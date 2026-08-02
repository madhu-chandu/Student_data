from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from config import session
import database_models
from models import Student,Course
from config import engine

app=FastAPI()
database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

@app.get("/Student")
def get_student(db:Session=Depends(get_db)):
    db_students=db.query(database_models.Students).all()
    return db_students

@app.get("/Student/{id}")
def get_student_by_id(id:int,db:Session=Depends(get_db)):
    db_student=db.query(database_models.Students).filter(database_models.Students.id==id).first()
    if db_student:
        return db_student
    return "Student not found"

@app.post("/Student")
def add_student(student:Student,db:Session=Depends(get_db)):
    db.add(database_models.Students(**student.model_dump()))
    db.commit()
    return student

@app.put("/Student/{id}")
def update_student(id:int,student:Student,db:Session=Depends(get_db)):
     db_student=db.query(database_models.Students).filter(database_models.Students.id==id).first()
     if db_student:
         db_student.name=student.name
         db_student.course_id=student.course_id
         db.commit()
         return "student details updated"
     return "student not found"

@app.delete("/Student/{id}")
def delete_student(id:int,db:Session=Depends(get_db)):
    db_student=db.query(database_models.Students).filter(database_models.Students.id==id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
        return "student deleted"
    return "student not found"

@app.post("/course")
def add_course(course:Course,db:Session=Depends(get_db)):
    db.add(database_models.Courses(**course.model_dump()))
    db.commit()
    return "course added"

@app.get("/course")
def get_course(db:Session=Depends(get_db)):
    db_course=db.query(database_models.Courses).all()
    return db_course

@app.get("/course/{id}")
def get_course_by_id(id:int,db:Session=Depends(get_db)):
    db_course=db.query(database_models.Courses).filter(database_models.Courses.id==id).first()
    if db_course:
        return db_course
    return "course not found"

@app.get("/student/{id}/course")
def get_course_student(id:int,db:Session=Depends(get_db)):
    db_student=db.query(database_models.Students).filter(database_models.Students.id==id).first()
    if db_student:
        return db_student.course
    return "student not found"

@app.get("/course/{id}/student")
def get_student_course(id:int,db:Session=Depends(get_db)):
    db_course=db.query(database_models.Courses).filter(database_models.Courses.id==id).first()
    if db_course:
        return db_course.students
    return "course not found"
    
    