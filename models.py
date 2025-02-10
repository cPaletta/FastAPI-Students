from sqlalchemy import Column, Integer, String
from database import Base
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
    role = Column(String)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)
    name = Column(String)  
    surname = Column(String)  
    phone = Column(String)  
