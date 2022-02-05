from bson.objectid import ObjectId

from server.database import student_collection, studentsHelper

async def get_all_students():
    students = []

    async for student in student_collection.find():
        students.append(studentsHelper(student))

    return students

async def add_student(student_data:dict)->dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({'_id':student.inserted_id})
    return studentsHelper(new_student)


async def get_student(id: str)->dict:
    student = await student_collection.find_one({'_id':ObjectId(id)})
    if student:
        return studentsHelper(student)

async def update_student(id:str, data:dict):
    if(len(data<1)):
        return False
    student = await student_collection.find_one({'_id':ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {'_id':ObjectId(id), '$set':data}
        )
        if update_student:
            return True
        return False

async def delete_student(id:str):
    student = await student_collection.find_one({'_id': ObjectId(id)})
    if student:
        await student_collection.delete_one({'_id':ObjectId(id)})
        return True
    return False