"""
usage
from app.schemas import CourseCreate, LessonResponse, ExerciseUpdate
"""

from ..schemas.course import CourseBase, CourseCreate, CourseResponse, CourseUpdate
from ..schemas.exercise import (
    ExerciseBase,
    ExerciseCreate,
    ExerciseResponse,
    ExerciseUpdate,
)
from ..schemas.lesson import LessonBase, LessonCreate, LessonResponse, LessonUpdate

__all__ = [
    # Course
    "CourseBase",
    "CourseCreate",
    "CourseUpdate",
    "CourseResponse",
    # Lesson
    "LessonBase",
    "LessonCreate",
    "LessonUpdate",
    "LessonResponse",
    # Exercise
    "ExerciseBase",
    "ExerciseCreate",
    "ExerciseUpdate",
    "ExerciseResponse",
]
