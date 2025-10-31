# controllers/data_manager.py
import json
from models.student import Student
from models.subject import Subject

DATA_FILE = "data/students.data"

class DataManager:
    """Save and load student data in JSON."""

    @staticmethod
    def saveData(students: list[Student]) -> None:
        blob = []
        for st in students:
            blob.append({
                "id": st.id,
                "name": st.name,
                "email": st.email,
                "password": st.password,
                "average_mark": st.average_mark,
                "pass_fail": st.pass_fail,
                "subjects": [
                    {"id": s.id, "name": s.name, "mark": s.mark, "grade": s.grade}
                    for s in st.subjects
                ]
            })
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(blob, f, indent=2)

    @staticmethod
    def loadData() -> list[Student]:
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                blob = json.load(f)
        except FileNotFoundError:
            return []

        students: list[Student] = []
        for st in blob:
            subjects = [Subject(**s) for s in st.get("subjects", [])]
            students.append(
                Student(
                    id=st["id"],
                    name=st["name"],
                    email=st["email"],
                    password=st["password"],
                    subjects=subjects,
                    average_mark=st.get("average_mark", 0.0),
                    pass_fail=st.get("pass_fail", "TBD"),
                )
            )
        return students
