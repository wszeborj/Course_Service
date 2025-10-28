"""
================
CRUD Operations:
- POST   /lessons              → Create lesson
- GET    /lessons              → List all lessons
- GET    /lessons/{id}         → Get specific lesson
- GET    /courses/{id}/lessons → Get lessons by course (NESTED!)
- PUT    /lessons/{id}         → Update lesson
- DELETE /lessons/{id}         → Delete lesson
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ... import crud
from ...db.session import get_db
from ...models import Lesson
from ...schemas import LessonCreate, LessonResponse, LessonUpdate

router = APIRouter()


@router.post(
    "",
    response_model=LessonResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new lesson",
)
def create_lesson(lesson: LessonCreate, db: Session = Depends(get_db)) -> Lesson:
    course = crud.get_course(db, course_id=lesson.course_id)
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {lesson.course_id} not found",
        )

    return crud.create_lesson(db=db, lesson=lesson)


@router.get(
    "",
    response_model=List[LessonResponse],
    summary="Get list of all lessons",
)
def get_lessons(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> List[Lesson]:
    lessons = crud.get_lessons(db, skip=skip, limit=limit)
    return lessons


@router.get(
    "/courses/{course_id}/lessons",
    response_model=List[LessonResponse],
    summary="Get lessons from specific course",
)
def get_lessons_by_course(
    course_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> List[Lesson]:
    course = crud.get_course(db, course_id=course_id)
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found",
        )

    lessons = crud.get_lessons_by_course(
        db, course_id=course_id, skip=skip, limit=limit
    )
    return lessons


@router.get(
    "/{lesson_id}",
    response_model=LessonResponse,
    summary="Get a specific lesson",
)
def get_lesson(lesson_id: int, db: Session = Depends(get_db)) -> Lesson:
    lesson = crud.get_lesson(db, lesson_id=lesson_id)

    if lesson is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lesson with id {lesson_id} not found",
        )

    return lesson


@router.put(
    "/{lesson_id}",
    response_model=LessonResponse,
    summary="Update a lesson",
)
def update_lesson(
    lesson_id: int, lesson_update: LessonUpdate, db: Session = Depends(get_db)
) -> Lesson:
    updated_lesson = crud.update_lesson(
        db, lesson_id=lesson_id, lesson_update=lesson_update
    )

    if updated_lesson is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lesson with id {lesson_id} not found",
        )

    return updated_lesson


@router.delete(
    "/{lesson_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a lesson",
)
def delete_lesson(lesson_id: int, db: Session = Depends(get_db)) -> None:
    success = crud.delete_lesson(db, lesson_id=lesson_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lesson with id {lesson_id} not found",
        )

    return None
