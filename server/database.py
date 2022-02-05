import motor.motor_asyncio


MONGO_DETAILS = 'mongodb://mongo:27017'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection('student_collection')


def studentsHelper(student)->dict:
    return {
        'id': str(student['_id']),
        'name': student['name'],
        'email': student['email'],
        'course_of_study': student['course_of_study'],
        'year':student['year']
    }

