from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import Student
from dependencies import get_db, get_current_admin_user
from pydantic import BaseModel, Field

router = APIRouter()

class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=1, le=120)
    year: str = Field(..., min_length=1, max_length=10)

@router.post("/students/", dependencies=[Depends(get_current_admin_user)])
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(name=student.name, age=student.age, year=student.year)
    try:
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Student with this ID already exists")
    return new_student

@router.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@router.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student