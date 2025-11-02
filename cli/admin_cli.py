# cli/admin_cli.py
from typing import Any, List
from controllers.admin_subsystem import AdminSubsystem


def admin_menu() -> None:
    admin = AdminSubsystem()

    while True:
        print("\n=== Admin System ===")
        print("1: View all students (brief)")
        print("2: View a student (id/email)")
        print("3: Remove a student (id)")
        print("4: Organise by grade  [HD/D/C/P/F]")
        print("5: Categorise PASS / FAIL")
        print("6: Cohort stats       [count, pass rate, grade mix]")
        print("X: Back to Main Menu")
        print("---------------------")
        choice = input("Enter choice: ").strip().upper()

        try:
            if choice == "1":
                _print_students_brief(admin.view_all_students())

            elif choice == "2":
                key = input("Enter id or email: ").strip()
                _view_student(admin.view_all_students(), key)

            elif choice == "3":
                sid = input("Enter student id to remove: ").strip()
                ok, msg = admin.remove_student(sid)
                print(msg if ok else f"[ERROR] {msg}")

            elif choice == "4":
                groups = admin.organise_by_grade()
                for g, lst in groups.items():
                    print(f"{g}: {[_name_id(s) for s in lst]}")

            elif choice == "5":
                buckets = admin.categorise_pass_fail()
                for k, lst in buckets.items():
                    print(f"{k}: {[_name_id(s) for s in lst]}")

            elif choice == "6":
                _print_cohort_stats(admin)

            elif choice == "X":
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"[UNEXPECTED ERROR] {e}")


# -------- helpers --------

def _get(obj: Any, key: str, default=None):
    return obj.get(key, default) if isinstance(obj, dict) else getattr(obj, key, default)

def _name_id(s: Any) -> str:
    sid = _get(s, "id") or _get(s, "studentID") or "?"
    return f"{_get(s, 'name', '?')}({sid})"

def _print_students_brief(students: List[Any]) -> None:
    if not students:
        print("[empty]")
        return
    print(f"{'ID':<8} {'NAME':<20} {'EMAIL':<28} {'SUBJ':>4} {'AVG':>6}  {'GRADE':>5} {'PF':>5}")
    print("-" * 75)
    for s in students:
        sid = _get(s, "id") or _get(s, "studentID") or ""
        name = _get(s, "name", "")
        email = _get(s, "email", "")
        subjects = _get(s, "subjects") or _get(s, "enrolments") or []
        avg = _get(s, "averageMark", "")
        grade = _get(s, "grade", _get(s, "overallGrade", ""))
        pf = _get(s, "passFailStatus", _get(s, "status", ""))
        print(f"{str(sid):<8} {str(name):<20} {str(email):<28} {len(subjects):>4} {str(avg):>6}  {str(grade):>5} {str(pf):>5}")

def _view_student(students: List[Any], key: str) -> None:
    key_norm = (key or "").strip().lower()
    found = None
    for s in students:
        sid = str(_get(s, "id") or _get(s, "studentID") or "").strip().lower()
        semail = str(_get(s, "email", "") or "").strip().lower()
        if key_norm in (sid, semail):
            found = s
            break
    if not found:
        print(f"[ERROR] Student '{key}' not found.")
        return
    print("--- Student record ---")
    if isinstance(found, dict):
        for k, v in found.items():
            print(f"{k}: {v}")
    else:
        for attr in ("id", "studentID", "name", "email", "subjects", "enrolments",
                     "averageMark", "grade", "overallGrade", "status", "passFailStatus"):
            print(f"{attr}: {getattr(found, attr, None)}")

def _print_cohort_stats(admin: AdminSubsystem) -> None:
    groups = admin.organise_by_grade()
    pf = admin.categorise_pass_fail()
    count = sum(len(v) for v in groups.values())
    pass_count = len(pf.get("PASS", []))
    pass_rate = (pass_count / count) if count else 0.0
    dist = {g: len(groups.get(g, [])) for g in ("HD", "D", "C", "P", "F")}
    print(f"Total students: {count}")
    print(f"Pass rate: {pass_rate:.2%}")
    print(f"Grade distribution: {dist}")