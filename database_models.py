from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
class Students(Base):
    __tablename__="Students"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100),nullable=False)
    course_id=Column(Integer,ForeignKey("Courses.id"))
    course=relationship("Courses", back_populates="students")

class Courses(Base):
    __tablename__="Courses"
    id=Column(Integer,primary_key=True,index=True)
    course_name=Column(String(100),nullable=False)
    students=relationship("Students",back_populates="course")