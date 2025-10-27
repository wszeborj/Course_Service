# Course CRUD operations
from ..crud.course import (
    create_course,
    get_course,
    get_courses,
    get_courses_count,
    update_course,
    delete_course,
)

# Lesson CRUD operations
from ..crud.lesson import (
    create_lesson,
    get_lesson,
    get_lessons,
    get_lessons_by_course,
    get_lessons_count,
    update_lesson,
    delete_lesson,
)

# Exercise CRUD operations
from ..crud.exercise import (
    create_exercise,
    get_exercise,
    get_exercises,
    get_exercises_by_lesson,
    get_exercises_count,
    update_exercise,
    delete_exercise,
)

# Export all CRUD functions
__all__ = [
    # Course operations
    "create_course",
    "get_course",
    "get_courses",
    "get_courses_count",
    "update_course",
    "delete_course",

    # Lesson operations
    "create_lesson",
    "get_lesson",
    "get_lessons",
    "get_lessons_by_course",
    "get_lessons_count",
    "update_lesson",
    "delete_lesson",

    # Exercise operations
    "create_exercise",
    "get_exercise",
    "get_exercises",
    "get_exercises_by_lesson",
    "get_exercises_count",
    "update_exercise",
    "delete_exercise",
]