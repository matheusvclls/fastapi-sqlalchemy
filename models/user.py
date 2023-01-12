import enum

from sqlalchemy import Boolean, Column, Integer, String, Enum

from db.db_setup import Base


class Role(enum.IntEnum):
    teacher = 1
    student = 2


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))
    is_active = Column(Boolean, default=False)
