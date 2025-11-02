# utils/validator.py
import re
import random
import utils.patterns as p

class Validator:

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Verifies that the email follows the correct format
        Example: firstname.lastname@university.com
        """
        return bool(re.fullmatch(p.EMAIL_PATTERN, email))

    @staticmethod
    def validate_password(password: str) -> tuple[bool, str]:
        if not re.fullmatch(p.PASSWORD_PATTERN, password):
            return False, "Password must start with uppercase, have 5+ letters, and 3+ digits."
        return True, "Password is valid"

    @staticmethod
    def generate_student_id(existing_ids: set = None) -> str:
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



def validate_email(email: str) -> bool:
    
    return Validator.validate_email(email)

def validate_password(password: str) -> bool:
  
    valid, msg = Validator.validate_password(password)
    return valid

def generate_student_id(existing_ids: set = None) -> str:
   
    return Validator.generate_student_id(existing_ids)