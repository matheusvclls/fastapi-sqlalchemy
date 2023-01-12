from sqlalchemy.orm import Session

from models.course import Course
from schemas.course import CourseCreate, CourseUpdate


async def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def get_courses(db: Session):
    return db.query(Course).all()


def get_user_courses(db: Session, user_id: int):
    courses = db.query(Course).filter(Course.user_id == user_id).all()
    return courses


def create_course(db: Session, course: CourseCreate):
    db_course = Course(
        title=course.title,
        description=course.description,
        user_id=course.user_id,
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def delete_course_by_id(db: Session, course_id: int):
    query = db.query(Course).get(course_id)
    db.delete(query)
    db.commit()
    db.close()
    return None


def update_course_by_id(db:Session,course_id, course: CourseUpdate):
    db_course = db.query(Course).get(course_id)
    course_data = course.dict(exclude_unset=True)
    for key, value in course_data.items():
        setattr(db_course, key, value)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    db.close()
    return db_course