from typing import Optional

from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    user_id: int


class CourseCreate(CourseBase):
    ...


class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True


class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    user_id: Optional[int]=None

    class Config:
        orm_mode = True
