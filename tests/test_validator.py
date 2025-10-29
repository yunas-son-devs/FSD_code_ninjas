# test_validator.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utils.patterns as p
from utils.validator import Validator

# Test 1: Email validation
print("=== Email Validation ===")
emails = [
    "john.doe@university.com",   # valid
    "JaneDoe@university.com",    # invalid
    "test@gmail.com",            # invalid
    "student@university",        # invalid
    "123@university.com",        # invalid
]
for email in emails:
    print(f"{email}: {Validator.validate_email(email)}")

# Test 2: Password validation
print("\n=== Password Validation ===")
passwords = [
    "Abcde123",     # ✅ valid
    "Aabcd12345",   # ✅ valid
    "abcde123",     # ❌ invalid 
    "Aabc12",       # ❌ invalid 
    "Abcde12",      # ❌ invalid 
]
for pwd in passwords:
    print(f"{pwd}: {Validator.validate_password(pwd)}")

# Test 3: Student ID generation
print("\n=== Student ID Generation ===")
existing = {"000001", "000002", "999999"}
new_id = Validator.generate_student_id(existing)
print(f"Generated ID: {new_id} (not in {existing})")
