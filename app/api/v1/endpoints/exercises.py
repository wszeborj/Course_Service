"""
CRUD Operations:
- POST   /exercises                → Create exercise
- GET    /exercises                → List all exercises
- GET    /exercises/{id}           → Get specific exercise
- GET    /lessons/{id}/exercises   → Get exercises by lesson (NESTED!)
- PUT    /exercises/{id}           → Update exercise
- DELETE /exercises/{id}           → Delete exercise
"""

from typing import List, Sequence

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .... import crud
from ....db.session import get_db
from ....models import Exercise
from ....schemas import ExerciseCreate, ExerciseResponse, ExerciseUpdate

router = APIRouter()


@router.post(
    "",
    response_model=ExerciseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new exercise",
)
async def create_exercise(
    exercise: ExerciseCreate, db: AsyncSession = Depends(get_db)
) -> Exercise:
    lesson = await crud.get_lesson(db, lesson_id=exercise.lesson_id)
    if lesson is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lesson with id {exercise.lesson_id} not found",
        )

    return await crud.create_exercise(db=db, exercise=exercise)


@router.get(
    "",
    response_model=List[ExerciseResponse],
    summary="Get list of all exercises",
)
async def get_exercises(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
) -> Sequence[Exercise]:
    exercises = await crud.get_exercises(db, skip=skip, limit=limit)
    return exercises


@router.get(
    "/lessons/{lesson_id}/exercises",
    response_model=List[ExerciseResponse],
    summary="Get exercises from specific lesson",
)
async def get_exercises_by_lesson(
    lesson_id: int, skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
) -> Sequence[Exercise]:
    lesson = await crud.get_lesson(db, lesson_id=lesson_id)
    if lesson is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lesson with id {lesson_id} not found",
        )

    exercises = await crud.get_exercises_by_lesson(
        db, lesson_id=lesson_id, skip=skip, limit=limit
    )
    return exercises


@router.get(
    "/{exercise_id}",
    response_model=ExerciseResponse,
    summary="Get a specific exercise",
)
async def get_exercise(
    exercise_id: int, db: AsyncSession = Depends(get_db)
) -> Exercise:
    exercise = await crud.get_exercise(db, exercise_id=exercise_id)

    if exercise is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Exercise with id {exercise_id} not found",
        )

    return exercise


@router.put(
    "/{exercise_id}",
    response_model=ExerciseResponse,
    summary="Update an exercise",
)
async def update_exercise(
    exercise_id: int,
    exercise_update: ExerciseUpdate,
    db: AsyncSession = Depends(get_db),
) -> Exercise:
    updated_exercise = await crud.update_exercise(
        db, exercise_id=exercise_id, exercise_update=exercise_update
    )

    if updated_exercise is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Exercise with id {exercise_id} not found",
        )

    return updated_exercise


@router.delete(
    "/{exercise_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete an exercise",
)
async def delete_exercise(exercise_id: int, db: AsyncSession = Depends(get_db)) -> None:
    success = await crud.delete_exercise(db, exercise_id=exercise_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Exercise with id {exercise_id} not found",
        )

    return None
