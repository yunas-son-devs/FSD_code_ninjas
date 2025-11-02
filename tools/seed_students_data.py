# tools/seed_students_data.py
# Generates data/students.data (pickle of list[dict]) for the whole team.

import os
import pickle

DATA_PATH = os.path.join("data", "students.data")

# ---------- helpers ----------
def grade_for(mark: float) -> str:
    # HD 85+, D 75–84, C 65–74, P 50–64, F <50
    if mark >= 85:
        return "HD"
    if mark >= 75:
        return "D"
    if mark >= 65:
        return "C"
    if mark >= 50:
        return "P"
    return "F"

def pass_fail_for(avg: float) -> str:
    return "PASS" if avg >= 50 else "FAIL"

# Canonical subjects requested
SUBJECTS = [
    ("PYT101", "Python Programming"),
    ("PRJ201", "Project Management"),
    ("SDEV210", "Software Development"),
    ("DBS210", "Database"),
    ("TRS300", "Technology Research"),
]

# Five students, same password, pre-assigned marks
ROWS = [
    {
        "id": "000201",
        "name": "Ved Chilimbi",
        "email": "ved.chilimbi@university.com",
        "password": "Abcde123",
        "marks": [88, 84, 91, 78, 85],  # PASS
    },
    {
        "id": "000202",
        "name": "John Doe",
        "email": "john.doe@university.com",
        "password": "Abcde123",
        "marks": [40, 47, 51, 38, 45],  # FAIL (avg < 50)
    },
    {
        "id": "000203",
        "name": "Yuna Son",
        "email": "yuna.son@university.com",
        "password": "Abcde123",
        "marks": [72, 68, 70, 66, 74],  # PASS (C grade level)
    },
    {
        "id": "000204",
        "name": "Suzy Lee",
        "email": "suzy.lee@university.com",
        "password": "Abcde123",
        "marks": [75, 81, 79, 68, 73],  # PASS
    },
    {
        "id": "000205",
        "name": "Vipin Kumar",
        "email": "vipin.kumar@university.com",
        "password": "Abcde123",
        "marks": [85, 88, 92, 80, 90],  # PASS (HD/D mix)
    },
]

def build_record(row: dict) -> dict:
    subjects = []
    for (code, name), mark in zip(SUBJECTS, row["marks"]):
        subjects.append({
            "code": code,
            "name": name,
            "mark": float(mark),
            "grade": grade_for(float(mark)),
        })
    avg = sum(row["marks"]) / len(row["marks"])
    return {
        "id": row["id"],
        "name": row["name"],
        "email": row["email"],
        "password": row["password"],        # plain, matches current system
        "subjects": subjects,               # list of dicts
        "averageMark": float(avg),
        "grade": grade_for(avg),            # top-level grade for admin views
        "passFailStatus": pass_fail_for(avg)
    }

def main():
    # Ensure folder exists
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

    # Backup any existing file so teammates don't lose local data
    if os.path.exists(DATA_PATH):
        try:
            os.replace(DATA_PATH, DATA_PATH + ".bak")
            print(f"[backup] moved old file to {DATA_PATH}.bak")
        except Exception as e:
            print(f"[backup] skip: {e}")

    # Build and write pickle
    students = [build_record(r) for r in ROWS]
    with open(DATA_PATH, "wb") as f:
        pickle.dump(students, f)

    print(f"[ok] wrote {len(students)} students to {DATA_PATH}")
    for s in students:
        print(f"- {s['id']} {s['name']}: avg={s['averageMark']:.2f}, grade={s['grade']}, {s['passFailStatus']}")

if __name__ == "__main__":
    main()