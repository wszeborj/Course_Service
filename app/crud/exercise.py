from sqlalchemy.orm import Session
from typing import List, Optional
from collections.abc import Sequence

from ..models import Exercise
from ..schemas import ExerciseCreate, ExerciseUpdate

def create_exercise(db: Session, exercise: ExerciseCreate) -> Exercise:
    db_exercise = Exercise(**exercise.model_dump())
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

def get_exercise(db: Session, exercise_id: int) -> Optional[Exercise]:
    return db.query(Exercise).filter(Exercise.id == exercise_id).first()

def get_exercises(
        db: Session,
        skip: int = 0,
        limit: int = 100
) -> list[Exercise]:
    return db.query(Exercise).offset(skip).limit(limit).all()


def get_exercises_by_lesson(
        db: Session,
        lesson_id: int,
        skip: int = 0,
        limit: int = 100
) -> Sequence[Exercise]:
    return (
        db.query(Exercise)
        .filter(Exercise.lesson_id == lesson_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_exercises_count(db: Session) -> int:
    return db.query(Exercise).count()

def update_exercise(
        db: Session,
        exercise_id: int,
        exercise_update: ExerciseUpdate
) -> Optional[Exercise]:
    db_exercise = get_exercise(db, exercise_id)
    if not db_exercise:
        return None

    update_data = exercise_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_exercise, field, value)

    db.commit()
    db.refresh(db_exercise)
    return db_exercise

def delete_exercise(db: Session, exercise_id: int) -> bool:
    db_exercise = get_exercise(db, exercise_id)
    if not db_exercise:
        return False

    db.delete(db_exercise)
    db.commit()
    return True
