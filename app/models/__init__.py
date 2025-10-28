"""
usage
from app.models import Course, Lesson, Exercise
"""

from typing import List

from ..models.course import Course
from ..models.exercise import Exercise
from ..models.lesson import Lesson

__all__: List = [Course, Lesson, Exercise]
