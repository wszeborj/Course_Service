"""
usage
from app.schemas import CourseCreate, LessonResponse, ExerciseUpdate
"""

from ..schemas.course import (
    CourseBase,
    CourseCreate,
    CourseUpdate,
    CourseResponse,
)

from ..schemas.lesson import (
    LessonBase,
    LessonCreate,
    LessonUpdate,
    LessonResponse,
)

from ..schemas.exercise import (
    ExerciseBase,
    ExerciseCreate,
    ExerciseUpdate,
    ExerciseResponse,
)

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