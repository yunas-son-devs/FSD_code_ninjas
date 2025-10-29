# controllers/student_subsystem.py

from typing import List, Dict 
from models.subject import Subject # Vipin's Subject model
# --- Dependencies from teammates ---
import utils.validator as validator       # Yuna's validation tools (Used as 'validator')
from controllers.data_manager import DataManager  # Ved's data persistence tools
import models.student as student_module # Vipin's Student model module import


class StudentSubsystem:
    MAX_SUBJECTS = 4

    def __init__(self):
        self.data_manager = DataManager()
        # Assumes student_module.Student is the class used in data loading
        self.all_students: List[student_module.Student] = self.data_manager.loadData()
        self.current_student: student_module.Student | None = None

    # ---------------- Registration/Login/Logout (YOUR GUI-READY LOGIC) ----------------
    
    def register(self, name: str, email: str, password: str) -> Dict:
        # 1. Input Validation 
        if not validator.validateEmail(email):
            return {"success": False, "message": "Registration failed: Invalid email format."}

        if not validator.validatePassword(password):
            return {"success": False, "message": "Registration failed: Password does not meet security requirements."}

        # 2. Existence Check
        for student_obj in self.all_students:
            if student_obj.email.lower() == email.lower():
                return {"success": False, "message": "Registration failed: This email is already registered."}

        # 3. Create New Student Object
        student_id = validator.generateStudentID()

        try:
            # Using Vipin's module import structure
            new_student = student_module.Student(student_id, name, email, password)
        except Exception as e:
            return {"success": False, "message": f"Error creating student object: {e}"}
        
        # 4. Data Persistence
        self.all_students.append(new_student) 

        if self.data_manager.saveData(self.all_students):
            return {"success": True, "message": f"Registration successful! Student ID: {student_id}"}
        else:
            self.all_students.pop() 
            return {"success": False, "message": "Registration failed: Could not save data to file."}

    def login(self, email: str, password: str) -> Dict:
        # 1. Find the User
        target_student = None
        for student_obj in self.all_students:
            if student_obj.email.lower() == email.lower():
                target_student = student_obj
                break
        
        if target_student is None:
            return {"success": False, "message": "Login failed: User not found."}

        # 2. Password Verification
        if target_student.password == password:
            # 3. Login Success
            self.current_student = target_student  
            return {"success": True, "student": target_student, "message": f"Login successful! Welcome, {target_student.name}."}
        else:
            return {"success": False, "message": "Login failed: Incorrect password."}

    def logout(self) -> Dict:
        if self.current_student is not None:
            name = self.current_student.name
            self.current_student = None 
            return {"success": True, "message": f"Logout successful. Goodbye, {name}."}
        else:
            return {"success": False, "message": "Error: No user is currently logged in."}

    # ---------------- Password Management (Vipin's Logic - Kept from HEAD) ----------------
    def change_password(self, new_password: str, confirm_password: str) -> bool:
        if not self.current_student:
            print("Error: No user logged in.")
            return False

        if new_password != confirm_password:
            print("Passwords do not match.")
            return False

        valid, msg = validator.validatePassword(new_password)
        if not valid:
            print(f"Password change failed: {msg}")
            return False

        self.current_student.password = new_password
        self.data_manager.saveData(self.all_students)
        print("Password changed successfully.")
        return True

    # ---------------- Subject Management (Vipin's Logic - Kept from HEAD) ----------------
    def enrol_subject(self, subject_name: str) -> bool:
        if not self.current_student:
            print("Error: No student logged in.")
            return False

        if len(self.current_student.subjects) >= self.MAX_SUBJECTS:
            print(f"Cannot enrol: Maximum of {self.MAX_SUBJECTS} subjects reached.")
            return False

        sub = Subject(id=Subject.generateSubjectID(), name=subject_name) 
        sub.autoAssignMark()
        sub.calculateGrade()
        self.current_student.subjects.append(sub)
        self.current_student.updateAverageMark()
        self.current_student.determinePassFailStatus()
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
            self.current_student.updateAverageMark()
            self.current_student.determinePassFailStatus()
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