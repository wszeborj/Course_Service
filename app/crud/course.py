from collections.abc import Sequence
from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Course
from ..schemas import CourseCreate, CourseUpdate


async def create_course(db: AsyncSession, course: CourseCreate) -> Course:
    db_course = Course(**course.model_dump())
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    return db_course


async def get_course(db: AsyncSession, course_id: int) -> Optional[Course]:
    stmt = select(Course).where(Course.id == course_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_courses(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> Sequence[Course]:
    stmt = select(Course).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_courses_count(db: AsyncSession) -> int:
    stmt = select(func.count()).select_from(Course)
    results = await db.execute(stmt)
    return results.scalar() or 0


async def update_course(
    db: AsyncSession, course_id: int, course_update: CourseUpdate
) -> Optional[Course]:
    db_course = await get_course(db, course_id)
    if not db_course:
        return None

    update_data = course_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_course, field, value)

    await db.commit()
    await db.refresh(db_course)
    return db_course


async def delete_course(db: AsyncSession, course_id: int) -> bool:
    db_course = await get_course(db, course_id)
    if not db_course:
        return False

    await db.delete(db_course)
    await db.commit()
    return True
