# controllers/admin_subsystem.py
from typing import Any, Dict, List
from controllers.data_manager import DataManager
from utils.academic_service import AcademicService

class AdminSubsystem:
    def __init__(self):
        self.data_manager = DataManager()

    def view_all_students(self) -> List[Any]:
        return self.data_manager.loadData()

    def remove_student(self, student_id: str) -> tuple[bool, str]:
        students = self.data_manager.loadData()
        idx = self._find_index(students, student_id)
        if idx is None:
            return False, f"Student {student_id} does not exist"
        students.pop(idx)
        self.data_manager.saveData(students)
        return True, f"Student {student_id} removed"

    def organise_by_grade(self) -> Dict[str, List[Any]]:
        groups: Dict[str, List[Any]] = {"HD": [], "D": [], "C": [], "P": [], "F": []}
        for s in self.data_manager.loadData():
            g = self._grade_for(s)
            groups[g if g in groups else "F"].append(s)
        return groups

    def categorise_pass_fail(self) -> Dict[str, List[Any]]:
        result = {"PASS": [], "FAIL": []}
        for s in self.data_manager.loadData():
            status = self._pass_fail_for(s)
            result[status].append(s)
        return result

    def clear_students(self) -> None:
        """Erase the students database (explicit action only)."""
        self.data_manager.clear()

    def summarize_student(self, s: Any) -> Dict[str, Any]:
        sid = self._get(s, "id") or self._get(s, "studentID") or "?"
        name = self._get(s, "name", "?")
        email = self._get(s, "email", "?")
        avg = self._avg_for(s) or 0.0
        grade = self._grade_for(s)
        pf = self._pass_fail_for(s)
        return {
            "id": sid,
            "name": name,
            "email": email,
            "avg": float(avg),
            "grade": grade,
            "passfail": pf,
            "subjects_count": len(self._subjects(s)),
        }

    def summaries(self) -> List[Dict[str, Any]]:
        return [self.summarize_student(s) for s in self.view_all_students()]

    def _find_index(self, students: List[Any], sid: str) -> int | None:
        for i, s in enumerate(students):
            if self._get(s, "studentID") == sid or self._get(s, "id") == sid:
                return i
        return None

    def _get(self, obj: Any, attr: str, default=None):
        return obj.get(attr, default) if isinstance(obj, dict) else getattr(obj, attr, default)

    def _subjects(self, s: Any) -> List[Any]:
        return self._get(s, "subjects") or self._get(s, "enrolments") or []

    def _avg_for(self, s: Any):
        avg = self._get(s, "averageMark")
        if isinstance(avg, (int, float)):
            return float(avg)
        marks = []
        for sub in self._subjects(s):
            mark = sub.get("mark") if isinstance(sub, dict) else getattr(sub, "mark", None)
            if isinstance(mark, (int, float)):
                marks.append(mark)
        return AcademicService.calculate_average(marks)

    def _grade_for(self, s: Any) -> str:
        g = self._get(s, "grade") or self._get(s, "overallGrade")
        if isinstance(g, str) and g in {"HD", "D", "C", "P", "F"}:
            return g
        return AcademicService.determine_grade(self._avg_for(s))

    def _pass_fail_for(self, s: Any) -> str:
        status = self._get(s, "status") or self._get(s, "passFailStatus")
        if isinstance(status, str) and status.upper() in {"PASS", "FAIL"}:
            return status.upper()
        return AcademicService.determine_pass_fail(self._avg_for(s))