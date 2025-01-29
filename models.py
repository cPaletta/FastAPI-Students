from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Enum
import enum

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    age = Column(Integer)
    year = Column(String)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)

    class RoleEnum(enum.Enum):
        admin = "admin"
        teacher = "teacher"
        student = "student"

    role = Column(Enum(RoleEnum))
    hashed_password = Column(String)
