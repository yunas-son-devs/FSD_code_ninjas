# utils/validator.py
import re
import random
import utils.patterns as p

class Validator:

    @staticmethod
    def validateEmail(email: str) -> bool:
        """
        Verifies that the email follows the correct format
        Example: firstname.lastname@university.com
        """
        return bool(re.fullmatch(p.EMAIL_PATTERN, email))

    @staticmethod
    def validatePassword(password: str) -> bool:
        """
        Checks if a password meets security rules:
        1. Starts with uppercase letter
        2. Minimum 5 letters
        3. Followed by at least 3 digits
        """
        return bool(re.fullmatch(p.PASSWORD_PATTERN, password))

    @staticmethod
    def generateStudentID(existing_ids: set = None) -> str:
        """
        Generates a unique 6-digit student ID (000001-999999)
        Ensures no collision with existing_ids if provided
        """
        if existing_ids is None:
            existing_ids = set()
        while True:
            student_id = f"{random.randint(1, 999999):06d}"
            if student_id not in existing_ids:
                return student_id
