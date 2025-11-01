# patterns.py

# Email Pattern Requirement: Must end with @university.com [cite: 91]
# Allows letters, numbers, dots, and underscores before the @.
EMAIL_PATTERN = r"^[A-Za-z]+[._-][A-Za-z]+@university\.com$"

# Password Pattern Requirements: [cite: 94]
# 1. ^[A-Z]       : Starts with an upper-case character.
# 2. [a-zA-Z]{4,} : Followed by five letters including the first character (total minimum length of 5 letters).
# 3. \d{3,}$     : Followed by three or more digits.
PASSWORD_PATTERN = r"^[A-Z][a-zA-Z]{4,}\d{3,}$"