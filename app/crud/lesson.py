from collections.abc import Sequence
from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Lesson
from ..schemas import LessonCreate, LessonUpdate


async def create_lesson(db: AsyncSession, lesson: LessonCreate) -> Lesson:
    db_lesson = Lesson(**lesson.model_dump())
    db.add(db_lesson)
    await db.commit()
    await db.refresh(db_lesson)
    return db_lesson


async def get_lesson(db: AsyncSession, lesson_id: int) -> Optional[Lesson]:
    stmt = select(Lesson).where(Lesson.id == lesson_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_lessons(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> Sequence[Lesson]:
    stmt = select(Lesson).offset(skip).limit(limit)
    results = await db.execute(stmt)
    return results.scalars().all()


async def get_lessons_by_course(
    db: AsyncSession, course_id: int, skip: int = 0, limit: int = 100
) -> Sequence[Lesson]:
    stmt = select(Lesson).where(Lesson.course_id == course_id).offset(skip).limit(limit)
    results = await db.execute(stmt)
    return results.scalars().all()


async def get_lessons_count(db: AsyncSession) -> int:
    stmt = select(func.count()).select_from(Lesson)
    result = await db.execute(stmt)
    return result.scalar() or 0


async def update_lesson(
    db: AsyncSession, lesson_id: int, lesson_update: LessonUpdate
) -> Optional[Lesson]:
    db_lesson = await get_lesson(db, lesson_id)
    if not db_lesson:
        return None

    update_data = lesson_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_lesson, field, value)

    await db.commit()
    await db.refresh(db_lesson)
    return db_lesson


async def delete_lesson(db: AsyncSession, lesson_id: int) -> bool:
    db_lesson = await get_lesson(db, lesson_id)
    if not db_lesson:
        return False

    await db.delete(db_lesson)
    await db.commit()
    return True
