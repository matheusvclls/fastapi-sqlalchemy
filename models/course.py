import enum

from sqlalchemy import  Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from db.db_setup import Base
from .user import User



class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_by = relationship(User)
