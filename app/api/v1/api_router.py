from fastapi import APIRouter

from ...api.v1.endpoints import courses, exercises, lessons

api_router = APIRouter()
api_router.include_router(courses.router, prefix="/courses", tags=["courses"])

api_router.include_router(lessons.router, prefix="/lessons", tags=["lessons"])

api_router.include_router(exercises.router, prefix="/exercises", tags=["exercises"])

"""
/api/v1/courses
/api/v1/courses/{id}
/api/v1/courses/{id}/lessons

/api/v1/lessons
/api/v1/lessons/{id}
/api/v1/lessons/{id}/exercises

/api/v1/exercises
/api/v1/exercises/{id}

"""
