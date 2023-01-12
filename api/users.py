from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from schemas.user import UserCreate, User, UserUpdate
from schemas.course import Course
from crud.users import get_user, get_user_by_email, get_users, create_user, delete_user_by_id,update_user_by_id
from crud.courses import get_user_courses

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Email is already registered"
        )
    return create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int,db: Session = Depends(get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/{user_id}/courses", response_model=List[Course])
async def read_user_courses(user_id: int, db: Session = Depends(get_db)):
    courses = get_user_courses(user_id=user_id, db=db)
    return courses

@router.delete('/user/{user_id}')
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    print(db_user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user_by_id(db=db,user_id=user_id)
    return f"User {user_id} deleted successfully"

@router.patch("/user/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_user = update_user_by_id(db=db,user_id=user_id, user=user)
    
    return db_user