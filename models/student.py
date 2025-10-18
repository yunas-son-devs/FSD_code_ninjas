# models/student.py
from dataclasses import dataclass, field
from typing import List
from utils.validator import Validator           # ← use central ID generator
from models.subject import Subject

@dataclass
class Student:
    id: str
    name: str
    email: str
    password: str
    subjects: List[Subject] = field(default_factory=list)
    average_mark: float = 0.0
    pass_fail: str = "TBD"

    MAX_SUBJECTS: int = 4

    @staticmethod
    def generateStudentID() -> str:
        """Get a random 6-digit Student ID from Validator"""
        return Validator.generateStudentID()

    def hasMaxSubjects(self) -> bool:
        return len(self.subjects) >= self.MAX_SUBJECTS
