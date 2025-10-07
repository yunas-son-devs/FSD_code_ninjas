# models/student.py
from dataclasses import dataclass, field
from typing import List
import random
from models.subject import Subject

@dataclass
class Student:
    id: str                   # "000001".."999999"
    name: str
    email: str
    password: str
    subjects: List[Subject] = field(default_factory=list)
    average_mark: float = 0.0
    pass_fail: str = "TBD"

    MAX_SUBJECTS: int = 4

    @staticmethod
    def generate_id() -> str:
        return f"{random.randint(1, 999_999):06d}"

    def hasMaxSubjects(self) -> bool:
        return len(self.subjects) >= self.MAX_SUBJECTS
