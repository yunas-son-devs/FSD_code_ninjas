import random

class Validator:
    @staticmethod
    def generateStudentID() -> str:
        """Create a random 6-digit Student ID"""
        return f"{random.randint(1, 999_999):06d}"
