from collections.abc import Sequence
from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Exercise
from ..schemas import ExerciseCreate, ExerciseUpdate


async def create_exercise(db: AsyncSession, exercise: ExerciseCreate) -> Exercise:
    db_exercise = Exercise(**exercise.model_dump())
    db.add(db_exercise)
    await db.commit()
    await db.refresh(db_exercise)
    return db_exercise


async def get_exercise(db: AsyncSession, exercise_id: int) -> Optional[Exercise]:
    stmt = select(Exercise).where(Exercise.id == exercise_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_exercises(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> Sequence[Exercise]:
    stmt = select(Exercise).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_exercises_by_lesson(
    db: AsyncSession, lesson_id: int, skip: int = 0, limit: int = 100
) -> Sequence[Exercise]:
    stmt = (
        select(Exercise)
        .where(Exercise.lesson_id == lesson_id)
        .offset(skip)
        .limit(limit)
    )
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_exercises_count(db: AsyncSession) -> int:
    stmt = select(func.count()).select_from(Exercise)
    result = await db.execute(stmt)
    return result.scalar() or 0


async def update_exercise(
    db: AsyncSession, exercise_id: int, exercise_update: ExerciseUpdate
) -> Optional[Exercise]:
    db_exercise = await get_exercise(db, exercise_id)
    if not db_exercise:
        return None

    update_data = exercise_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_exercise, field, value)

    await db.commit()
    await db.refresh(db_exercise)
    return db_exercise


async def delete_exercise(db: AsyncSession, exercise_id: int) -> bool:
    db_exercise = await get_exercise(db, exercise_id)
    if not db_exercise:
        return False

    await db.delete(db_exercise)
    await db.commit()
    return True
