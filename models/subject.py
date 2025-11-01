# models/subject.py
from dataclasses import dataclass, field
import random

@dataclass
class Subject:
    id: str
    name: str
    mark: int = field(default=0)
    grade: str = field(default="Not graded")

    @staticmethod
    def generate_subject_id() -> str:
        """Create a random 3-digit Subject ID"""
        return f"{random.randint(1, 999):03d}"

    def assign_mark(self):
        """Assign a random mark between 25 and 100"""
        self.mark = random.randint(25, 100)

    def calculate_grade(self):
        """Convert numeric mark to letter grade"""
        if self.mark >= 85:
            self.grade = "HD"
        elif self.mark >= 75:
            self.grade = "D"
        elif self.mark >= 65:
            self.grade = "C"
        elif self.mark >= 50:
            self.grade = "P"
        else:
            self.grade = "F"
