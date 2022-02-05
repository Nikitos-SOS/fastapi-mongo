from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.crud import (
    add_student,
    get_all_students,
    get_student,
    update_student,
    delete_student
)

from server.models.student import (
    StudentModel,
    UpdateStudentModel,
    ErrorResponseModel,
    ResponseModel
)

router = APIRouter()

@router.post('/', response_description='Add student data to database')
async def add_student_data( student: StudentModel=Body(...) ):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, 'Student was added successfully')

@router.get('/all', response_description='List of all students')
async def get_all_students_data( ):
    students = await get_all_students()
    if students:
        return ResponseModel(students, 'List of students')
    return ResponseModel(students, 'Empty list of students')

@router.get('/{id}', response_description='Get student with concriate id')
async def get_student_by_id(id):
    student = await get_student(id)
    if student:
        return ResponseModel(student, f'Student with id = {id}')
    return ErrorResponseModel('An error accured', 404, 'Student doesnt exist!')

@router.put('/{id}', response_description="Update student's data")
async def update_student_data(id, req:UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(id,req)
    if updated_student:
        return ResponseModel(updated_student, 'Successfully')
    return ErrorResponseModel('An error accured', 404, 'Somethig went wrong')

@router.delete('/{id}', response_description='Delete student from db')
async def delete_student_data(id):
    deleted_student = await delete_student(id)
    if deleted_student:
        return ResponseModel(deleted_student, 'Deleted successfuly')
    return ErrorResponseModel('An error accured', 404, 'Something went wrong')