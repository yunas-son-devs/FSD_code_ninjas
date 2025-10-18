import random

class Validator:
    @staticmethod
    def generateStudentID() -> str:
        return f"{random.randint(1, 999_999):06d}"
