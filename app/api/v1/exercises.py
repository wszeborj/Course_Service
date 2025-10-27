"""
CRUD Operations:
- POST   /exercises                → Create exercise
- GET    /exercises                → List all exercises
- GET    /exercises/{id}           → Get specific exercise
- GET    /lessons/{id}/exercises   → Get exercises by lesson (NESTED!)
- PUT    /exercises/{id}           → Update exercise
- DELETE /exercises/{id}           → Delete exercise
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ...db.session import get_db
from ...schemas import ExerciseCreate, ExerciseUpdate, ExerciseResponse
from ... import crud

router = APIRouter()

@router.post(
    "",
    response_model=ExerciseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new exercise",
)
def create_exercise(
        exercise: ExerciseCreate,
        db: Session = Depends(get_db)
) -> ExerciseResponse:
    lesson = crud.get_lesson(db, lesson_id=exercise.lesson_id)
    if lesson is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lesson with id {exercise.lesson_id} not found"
        )

    return crud.create_exercise(db=db, exercise=exercise)


@router.get(
    "",
    response_model=List[ExerciseResponse],
    summary="Get list of all exercises",
)
def get_exercises(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
) -> List[ExerciseResponse]:
    """
    Retrieve list of all exercises from all lessons.
    """
    exercises = crud.get_exercises(db, skip=skip, limit=limit)
    return exercises

@router.get(
    "/lessons/{lesson_id}/exercises",
    response_model=List[ExerciseResponse],
    summary="Get exercises from specific lesson",
)
def get_exercises_by_lesson(
        lesson_id: int,
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
) -> List[ExerciseResponse]:

    lesson = crud.get_lesson(db, lesson_id=lesson_id)
    if lesson is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lesson with id {lesson_id} not found"
        )

    exercises = crud.get_exercises_by_lesson(
        db,
        lesson_id=lesson_id,
        skip=skip,
        limit=limit
    )
    return exercises

@router.get(
    "/{exercise_id}",
    response_model=ExerciseResponse,
    summary="Get a specific exercise",
)
def get_exercise(
        exercise_id: int,
        db: Session = Depends(get_db)
) -> ExerciseResponse:

    exercise = crud.get_exercise(db, exercise_id=exercise_id)

    if exercise is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Exercise with id {exercise_id} not found"
        )

    return exercise


@router.put(
    "/{exercise_id}",
    response_model=ExerciseResponse,
    summary="Update an exercise",
)
def update_exercise(
        exercise_id: int,
        exercise_update: ExerciseUpdate,
        db: Session = Depends(get_db)
) -> ExerciseResponse:

    updated_exercise = crud.update_exercise(
        db,
        exercise_id=exercise_id,
        exercise_update=exercise_update
    )

    if updated_exercise is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Exercise with id {exercise_id} not found"
        )

    return updated_exercise

@router.delete(
    "/{exercise_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an exercise",
)
def delete_exercise(
        exercise_id: int,
        db: Session = Depends(get_db)
) -> None:

    success = crud.delete_exercise(db, exercise_id=exercise_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Exercise with id {exercise_id} not found"
        )

    return None