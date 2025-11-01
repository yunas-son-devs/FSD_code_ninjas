from typing import List, Dict
from models.student import Student
from models.subject import Subject
from utils.validator import Validator
from controllers.data_manager import DataManager

class StudentSubsystem:
    """
    Handles student-facing operations:
    - Registration/Login/Logout
    - Password change
    - Subject enrolment/removal/view
    All data is persisted via DataManager.
    """

    MAX_SUBJECTS = 4

    def __init__(self):
        self.data_manager = DataManager()          # Ved's persistence
        self.all_students: List[Student] = self.data_manager.loadData()
        self.current_student: Student | None = None

    # ---------------- Registration/Login/Logout ----------------
    def register(self, name: str, email: str, password: str) -> bool:
        # Email validation
        if not Validator.validate_email(email):
            print("Registration failed: Invalid email format.")
            return False

        # Password validation
        valid, msg = Validator.validate_password(password)
        if not valid:
            print(f"Registration failed: {msg}")
            return False

        # Check for duplicate email
        for student_obj in self.all_students:
            if student_obj.email.lower() == email.lower():
                print("Registration failed: Email already registered.")
                return False

        # Generate unique student ID
        student_id = Validator.generate_student_id()
        try:
            new_student = Student(student_id, name, email, password)
        except Exception as e:
            print(f"Error creating student object: {e}")
            return False

        self.all_students.append(new_student)
        try:
            self.data_manager.saveData(self.all_students)
            print(f"Registration successful! Student ID: {student_id}")
            return True
        except Exception:
            self.all_students.pop()
            print("Registration failed: Could not save data.")
            return False

    def login(self, email: str, password: str) -> bool:
        for student_obj in self.all_students:
            if student_obj.email.lower() == email.lower():
                if student_obj.password == password:
                    self.current_student = student_obj
                    print(f"Login successful! Welcome, {student_obj.name}.")
                    return True
                else:
                    print("Login failed: Incorrect password.")
                    return False
        print("Login failed: User not found.")
        return False

    def logout(self) -> bool:
        if self.current_student:
            name = self.current_student.name
            self.current_student = None
            print(f"Logout successful. Goodbye, {name}.")
            return True
        print("Logout failed: No user is currently logged in.")
        return False

    # ---------------- Password Management ----------------
    def change_password(self, new_password: str, confirm_password: str) -> bool:
        if not self.current_student:
            print("Error: No user logged in.")
            return False

        if new_password != confirm_password:
            print("Passwords do not match.")
            return False

        valid, msg = Validator.validate_password(new_password)
        if not valid:
            print(f"Password change failed: {msg}")
            return False

        self.current_student.password = new_password
        self.data_manager.saveData(self.all_students)
        print("Password changed successfully.")
        return True

    # ---------------- Subject Management ----------------
    def enrol_subject(self, subject_name: str) -> bool:
        if not self.current_student:
            print("Error: No student logged in.")
            return False

        if len(self.current_student.subjects) >= self.MAX_SUBJECTS:
            print(f"Cannot enrol: Maximum of {self.MAX_SUBJECTS} subjects reached.")
            return False

        sub = Subject(id=Subject.generate_subject_id(), name=subject_name)
        sub.assign_mark()
        sub.calculate_grade()
        self.current_student.subjects.append(sub)
        self.current_student.update_average_mark()
        self.current_student.determine_pass_fail_status()
        self.data_manager.saveData(self.all_students)
        print(f"Enrolled in subject '{subject_name}' successfully.")
        return True

    def remove_subject(self, subject_id: str) -> bool:
        if not self.current_student:
            print("Error: No student logged in.")
            return False

        before = len(self.current_student.subjects)
        self.current_student.subjects = [
            s for s in self.current_student.subjects if s.id != subject_id
        ]
        removed = len(self.current_student.subjects) < before

        if removed:
            self.current_student.update_average_mark()
            self.current_student.determine_pass_fail_status()
            self.data_manager.saveData(self.all_students)
            print(f"Removed subject {subject_id} successfully.")
        else:
            print(f"Subject {subject_id} not found.")
        return removed

    def view_enrolments(self) -> List[Dict]:
        if not self.current_student:
            print("Error: No student logged in.")
            return []
        return [
            {"id": s.id, "name": s.name, "mark": s.mark, "grade": s.grade}
            for s in self.current_student.subjects
        ]
