from typing import Optional, List
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

courses = []



@router.get("/courses")
async def get_courses():
    return courses


@router.post("/courses")
async def create_course():
    courses.append()
    return "Success"


@router.get("/courses/{id}")
async def get_course(id: int):
    return { "course": courses[id] }