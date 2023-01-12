from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from schemas.course import Course, CourseCreate, CourseUpdate
from crud.courses import get_course, get_courses, create_course,delete_course_by_id, update_course_by_id

router = fastapi.APIRouter()


@router.get("/courses", response_model=List[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses


@router.post("/courses", response_model=Course)
async def create_new_course(
    course: CourseCreate, db: Session = Depends(get_db)
):
    return create_course(db=db, course=course)


@router.get("/courses/{course_id}")
async def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@router.delete('/courses/{course_id}')
def delete_course(course_id: int, db: Session = Depends(get_db)):
    db_user = get_course(db=db, course_id=course_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    delete_course_by_id(db=db,course_id=course_id)
    return f"Course {course_id} deleted successfully"


@router.patch("/courses/{course_id}", response_model=Course)
async def update_user(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    db_course = await get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    db_course = update_course_by_id(db=db,course_id=course_id, course=course)
    
    return db_course