"""
CRUD Operations:
- POST   /courses          → Create course
- GET    /courses          → List all courses
- GET    /courses/{id}     → Get specific course
- PUT    /courses/{id}     → Update course
- DELETE /courses/{id}     → Delete course
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ...db.session import get_db
from ...schemas import CourseCreate, CourseUpdate, CourseResponse
from ... import crud

router = APIRouter()

@router.post(
    "",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new course",
)
def create_course(
        course: CourseCreate,
        db: Session = Depends(get_db)
):

    return crud.create_course(db=db, course=course)

@router.get(
    "",
    response_model=List[CourseResponse],
    summary="Get list of courses",
)
def get_courses(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
):

    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses

@router.get(
    "/{course_id}",
    response_model=CourseResponse,
    summary="Get a specific course",
)
def get_course(
        course_id: int,
        db: Session = Depends(get_db)
):

    course = crud.get_course(db, course_id=course_id)

    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found"
        )

    return course

@router.put(
    "/{course_id}",
    response_model=CourseResponse,
    summary="Update a course",
)
def update_course(
        course_id: int,
        course_update: CourseUpdate,
        db: Session = Depends(get_db)
):

    updated_course = crud.update_course(
        db,
        course_id=course_id,
        course_update=course_update
    )

    if updated_course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found"
        )

    return updated_course


@router.delete(
    "/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a course",
)
def delete_course(
        course_id: int,
        db: Session = Depends(get_db)
):

    success = crud.delete_course(db, course_id=course_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found"
        )

    return None

