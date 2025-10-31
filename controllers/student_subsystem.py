from controllers.data_manager import DataManager
# controllers/student_subsystem.py
from typing import List, Dict
from models.student import Student
from models.subject import Subject
from utils.validator import Validator

class StudentSubsystem:
    """Student-facing operations for enrolment, removal, viewing, and password change."""

    def __init__(self, current_student: Student):
        self.student = current_student

    def enrolSubject(self, subject_name: str) -> Subject:
        if self.student.hasMaxSubjects():
            raise ValueError("Cannot enrol: student already has 4 subjects.")
        if any(s.name.lower() == subject_name.lower() for s in self.student.subjects):
            raise ValueError("Subject already enrolled.")
        

        sub = Subject(id=Subject.generateSubjectID(), name=subject_name)
        sub.assign_mark()
        sub.calculate_grade()
        self.student.subjects.append(sub)

        self.student.update_average_mark()
        self.student.determine_pass_fail_status()
        DataManager.saveData([self.student])

        return sub

    def removeSubject(self, subject_id: str) -> bool:
        before = len(self.student.subjects)
        self.student.subjects = [s for s in self.student.subjects if s.id != subject_id]
        removed = len(self.student.subjects) != before

        self.student.update_average_mark()
        self.student.determine_pass_fail_status()
        DataManager.saveData([self.student])

        return removed

    def viewEnrolments(self) -> List[Dict]:
        return [
            {"id": s.id, "name": s.name, "mark": s.mark, "grade": s.grade}
            for s in self.student.subjects
        ]

    def changePassword(self, new_password: str, confirm_password: str) -> None:
        if new_password != confirm_password:
            raise ValueError("Passwords do not match.")
        if hasattr(Validator, "validatePassword"):
            ok, msg = Validator.validatePassword(new_password)
            if not ok:
                raise ValueError(msg)
        self.student.password = new_password
