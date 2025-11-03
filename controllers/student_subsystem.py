from typing import List, Dict
from models.student import Student
from models.subject import Subject
from utils.validator import Validator
from controllers.data_manager import DataManager

class StudentSubsystem:
    MAX_SUBJECTS = 4

    def __init__(self):
        self.data_manager = DataManager()
        self.all_students: List[Student] = self.data_manager.loadData()
        self.current_student: Student | None = None

    def _reload(self) -> None:
        self.all_students = self.data_manager.loadData()

    def _save(self) -> None:
        self.data_manager.saveData(self.all_students)
        self._reload()

    def _find_index_by_id(self, sid: str) -> int | None:
        for i, s in enumerate(self.all_students):
            if str(getattr(s, "id", getattr(s, "studentID", ""))) == str(sid):
                return i
        return None

    def _find_by_email(self, email: str) -> Student | None:
        email_l = (email or "").strip().lower()
        for s in self.all_students:
            if getattr(s, "email", "").strip().lower() == email_l:
                return s
        return None

    def _ensure_current_is_fresh(self) -> Student | None:
        if not self.current_student:
            return None
        sid = str(getattr(self.current_student, "id", getattr(self.current_student, "studentID", "")))
        idx = self._find_index_by_id(sid)
        if idx is None:
            self.current_student = None
            return None
        self.current_student = self.all_students[idx]
        return self.current_student

    def register(self, name: str, email: str, password: str) -> bool:
        self._reload()
        if not Validator.validate_email(email):
            print("Registration failed: Invalid email format.")
            return False
        valid, msg = Validator.validate_password(password)
        if not valid:
            print(f"Registration failed: {msg}")
            return False
        if self._find_by_email(email):
            print("Registration failed: Email already registered.")
            return False
        student_id = Validator.generate_student_id()
        try:
            new_student = Student(student_id, name, email, password)
        except Exception as e:
            print(f"Error creating student object: {e}")
            return False
        self.all_students.append(new_student)
        try:
            self._save()
            print(f"Registration successful! Student ID: {student_id}")
            return True
        except Exception:
            if self.all_students and getattr(self.all_students[-1], "id", None) == student_id:
                self.all_students.pop()
            print("Registration failed: Could not save data.")
            return False

    def login(self, email: str, password: str) -> bool:
        self._reload()
        student_obj = self._find_by_email(email)
        if student_obj is None:
            print("Login failed: User not found.")
            return False
        if student_obj.password != password:
            print("Login failed: Incorrect password.")
            return False
        self.current_student = student_obj
        print(f"Login successful! Welcome, {student_obj.name}.")
        return True

    def logout(self) -> bool:
        if self.current_student:
            name = self.current_student.name
            self.current_student = None
            print(f"Logout successful. Goodbye, {name}.")
            return True
        print("Logout failed: No user is currently logged in.")
        return False

    def change_password(self, new_password: str, confirm_password: str) -> bool:
        self._reload()
        if not self._ensure_current_is_fresh():
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
        self._save()
        print("Password changed successfully.")
        return True

    def enrol_subject(self, subject_name: str) -> bool:
        self._reload()
        if not self._ensure_current_is_fresh():
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
        self._save()
        print(f"Enrolled in subject '{subject_name}' successfully.")
        return True

    def remove_subject(self, subject_id: str) -> bool:
        self._reload()
        if not self._ensure_current_is_fresh():
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
            self._save()
            print(f"Removed subject {subject_id} successfully.")
        else:
            print(f"Subject {subject_id} not found.")
        return removed

    def view_enrolments(self) -> List[Dict]:
        self._reload()
        if not self._ensure_current_is_fresh():
            print("Error: No student logged in.")
            return []
        return [
            {"id": s.id, "name": s.name, "mark": s.mark, "grade": s.grade}
            for s in self.current_student.subjects
        ]