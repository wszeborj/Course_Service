"""
CRUD Operations:
- POST   /courses          → Create course
- GET    /courses          → List all courses
- GET    /courses/{id}     → Get specific course
- PUT    /courses/{id}     → Update course
- DELETE /courses/{id}     → Delete course
"""

from typing import List, Sequence

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .... import crud
from ....db.session import get_db
from ....models import Course
from ....schemas import CourseCreate, CourseResponse, CourseUpdate

router = APIRouter()


@router.post(
    "",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new course",
)
async def create_course(
    course: CourseCreate, db: AsyncSession = Depends(get_db)
) -> Course:
    return await crud.create_course(db=db, course=course)


@router.get(
    "",
    response_model=List[CourseResponse],
    summary="Get list of courses",
)
async def get_courses(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
) -> Sequence[Course]:
    courses = await crud.get_courses(db, skip=skip, limit=limit)
    return courses


@router.get(
    "/{course_id}",
    response_model=CourseResponse,
    summary="Get a specific course",
)
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)) -> Course:
    course = await crud.get_course(db, course_id=course_id)

    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found",
        )

    return course


@router.put(
    "/{course_id}",
    response_model=CourseResponse,
    summary="Update a course",
)
async def update_course(
    course_id: int, course_update: CourseUpdate, db: AsyncSession = Depends(get_db)
) -> Course:
    updated_course = await crud.update_course(
        db, course_id=course_id, course_update=course_update
    )

    if updated_course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found",
        )

    return updated_course


@router.delete(
    "/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a course",
)
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)) -> None:
    success = await crud.delete_course(db, course_id=course_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found",
        )

    return None
