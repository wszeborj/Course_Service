from sqlalchemy.orm import Session
from typing import List, Optional

from ..models import Lesson
from ..schemas import LessonCreate, LessonUpdate

def create_lesson(db: Session, lesson: LessonCreate) -> Lesson:
    db_lesson = Lesson(**lesson.model_dump(exclude={'exercises'}))
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

def get_lesson(db: Session, lesson_id: int) -> Optional[Lesson]:
    return db.query(Lesson).filter(Lesson.id == lesson_id).first()

def get_lessons(
        db: Session,
        skip: int = 0,
        limit: int = 100
) -> List[Lesson]:
    return db.query(Lesson).offset(skip).limit(limit).all()


def get_lessons_by_course(
        db: Session,
        course_id: int,
        skip: int = 0,
        limit: int = 100
) -> List[Lesson]:
    return (
        db.query(Lesson)
        .filter(Lesson.course_id == course_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_lessons_count(db: Session) -> int:
    return db.query(Lesson).count()

def update_lesson(
        db: Session,
        lesson_id: int,
        lesson_update: LessonUpdate
) -> Optional[Lesson]:
    db_lesson = get_lesson(db, lesson_id)
    if not db_lesson:
        return None

    update_data = lesson_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_lesson, field, value)

    db.commit()
    db.refresh(db_lesson)
    return db_lesson

def delete_lesson(db: Session, lesson_id: int) -> bool:
    db_lesson = get_lesson(db, lesson_id)
    if not db_lesson:
        return False

    db.delete(db_lesson)
    db.commit()
    return True
