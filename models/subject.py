# models/subject.py
from dataclasses import dataclass, field
import random

@dataclass
class Subject:
    id: str                   # "001".."999"
    name: str                 # e.g., "FSD"
    mark: int = field(default=0)
    grade: str = field(default="Not graded")

    @staticmethod
    def generate_id() -> str:
        return f"{random.randint(1, 999):03d}"

    def assign_mark(self) -> None:
        self.mark = random.randint(25, 100)

    def calculate_grade(self) -> None:
        m = self.mark
        if   m >= 85: self.grade = "HD"
        elif m >= 75: self.grade = "D"
        elif m >= 65: self.grade = "C"
        elif m >= 50: self.grade = "P"
        else:         self.grade = "F"
