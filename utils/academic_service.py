from typing import Iterable, Optional

class AcademicService:
    @staticmethod
    def calculate_average(marks: Iterable[float]) -> Optional[float]:
        nums = [float(m) for m in marks if isinstance(m, (int, float))]
        return sum(nums)/len(nums) if nums else None

    @staticmethod
    def determine_grade(avg: Optional[float]) -> str:
        if avg is None: return "F"
        if avg >= 85: return "HD"
        if avg >= 75: return "D"
        if avg >= 65: return "C"
        if avg >= 50: return "P"
        return "F"

    @staticmethod
    def determine_pass_fail(avg: Optional[float]) -> str:
        return "PASS" if (avg is not None and avg >= 50) else "FAIL"
