from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# create api
app2 = FastAPI()

app2.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# define a class Student that inherits from BaseModel
class Student(BaseModel):
    id: int
    name: str
    grade: int

# list for store the data
students = [
    Student(id=1, name="Hamza Mohamed", grade=8),
    Student(id=2, name="Yassin Mohamed", grade=5),
]

# read the students
@app2.get("/students/")
def read_student():
    return students

# add student
@app2.post('/students/')
def create_student(New_student: Student):
    students.append(New_student)
    return New_student

# edit students
@app2.put("/students/{student_id}")
def update_student(student_id: int, update_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = update_student
            return update_student
    return {"error" : "Student not found"}


@app2.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message" : "Student deleted successfully"}
    return {"error" : "student not found"}
