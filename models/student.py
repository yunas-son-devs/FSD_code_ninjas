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

    def update_average_mark(self) -> None:
        """Recalculate the student's overall average from enrolled subjects."""
        if not self.subjects:
            self.average_mark = 0.0
            return
        total = sum(s.mark for s in self.subjects)
        self.average_mark = round(total / len(self.subjects), 2)

    def determine_pass_fail_status(self) -> None:
        """Set PASS if average >= 50 else FAIL."""
        self.pass_fail = "PASS" if self.average_mark >= 50 else "FAIL"





    @staticmethod
    def generateStudentID() -> str:
        """Get a random 6-digit Student ID from Validator"""
        return Validator.generateStudentID()

    def hasMaxSubjects(self) -> bool:
        return len(self.subjects) >= self.MAX_SUBJECTS
