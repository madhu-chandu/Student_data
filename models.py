from pydantic import BaseModel

class Course(BaseModel):
    id:int
    course_name:str

class Student(BaseModel):
    id:int
    name:str
    course_id:int
    