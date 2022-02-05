from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class StudentModel(BaseModel):
    name: str = Field(...)
    email:EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)

    class Config:
        schema_extra={
            "example":{
                'name':'Ivan',
                'email':'example@gmail.com',
                'course_of_study': 'Mathumatica',
                'year': 3,
            }
        }

class UpdateStudentModel(BaseModel):
    name:Optional[str]
    email:Optional[EmailStr]
    course_of_study:Optional[str]
    year:Optional[int]

    class Config:
        schema_extra={
            "example":{
                'name':'Ivan',
                'email':'example@gmail.com',
                'course_of_study': 'Mathumatica',
                'year': 3,
            }
        }
def ResponseModel(data,message):
    return {
        'data':[data],
        'code':200,
        'message':message
    }

def ErrorResponseModel(error, code, message):
    return{
        'error':error,
        'code':code,
        'message':message
    }