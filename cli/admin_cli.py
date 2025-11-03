# cli/admin_cli.py
from typing import Any, List, Dict
from controllers.admin_subsystem import AdminSubsystem

# ---- simple ANSI styling (works in VS Code terminal/Windows 10+ PowerShell) ----
class S:
    B = "\033[1m"
    DIM = "\033[2m"
    R = "\033[0m"
    CY = "\033[36m"
    GR = "\033[32m"
    YL = "\033[33m"
    RD = "\033[31m"
    BL = "\033[34m"

ADMIN_PASSWORD = "Abcde123"

def admin_menu() -> None:
    # visible password prompt
    print(f"\n{S.B}{S.BL}=== Admin Login ==={S.R}")
    pwd = input("Enter admin password: ").strip()
    if pwd != ADMIN_PASSWORD:
        print(f"{S.RD}Access denied.{S.R}")
        return

    admin = AdminSubsystem()

    while True:
        print(f"\n{S.B}{S.BL}=== Admin System ==={S.R}")
        print("1: View all students (brief)")
        print("2: View a student (id/email)")
        print("3: Remove a student (id)")
        print("4: Organise by grade  [HD/D/C/P/F]")
        print("5: Categorise PASS / FAIL")
        print("6: Cohort stats       [count, pass rate, grade mix]")
        print("7: Clear students database")
        print("X: Back to Main Menu")
        print(S.DIM + "-" * 29 + S.R)
        choice = input("Enter choice: ").strip().upper()

        try:
            if choice == "1":
                _print_students_lines(admin)

            elif choice == "2":
                key = input("Enter id or email: ").strip()
                _view_student(admin, key)

            elif choice == "3":
                sid = input("Remove by ID: ").strip()
                print(f"{S.YL}Removing Student {sid} Account{S.R}")
                ok, msg = admin.remove_student(sid)
                print(msg if ok else f"{S.RD}{msg}{S.R}")

            elif choice == "4":
                _print_grade_groups(admin)

            elif choice == "5":
                _print_pass_fail(admin)

            elif choice == "6":
                _print_cohort_stats(admin)

            elif choice == "7":
                _clear_database_flow(admin)

            elif choice == "X":
                break
            else:
                print(f"{S.RD}Invalid choice.{S.R}")
        except Exception as e:
            print(f"{S.RD}[UNEXPECTED ERROR] {e}{S.R}")


# -------- helpers --------

def _fmt_name_id_email(s: Dict[str, Any]) -> str:
    return f"{s['name']} :: {s['id']} --> Email: {s['email']}"

def _fmt_name_grade_mark(s: Dict[str, Any]) -> str:
    return f"{s['name']} :: {s['id']} --> GRADE: {s['grade']} - MARK: {s['avg']:.2f}"

def _print_header(text: str, color=S.GR):
    print(f"{S.B}{color}{text}{S.R}")

def _print_students_lines(admin: AdminSubsystem) -> None:
    students = admin.summaries()
    _print_header("Student List", S.GR)
    if not students:
        print(S.DIM + "< Nothing to Display >" + S.R)
        return
    for s in students:
        print(_fmt_name_id_email(s))

def _view_student(admin: AdminSubsystem, key: str) -> None:
    key_norm = (key or "").strip().lower()
    for s in admin.summaries():
        if key_norm in (str(s["id"]).lower(), str(s["email"]).lower()):
            _print_header("Student Record", S.CY)
            for k in ("id", "name", "email", "avg", "grade", "passfail", "subjects_count"):
                print(f"{k}: {s.get(k)}")
            return
    print(f"{S.RD}Student '{key}' not found.{S.R}")

def _print_grade_groups(admin: AdminSubsystem) -> None:
    _print_header("Grade Grouping", S.CY)
    groups = admin.organise_by_grade()
    by_grade: Dict[str, List[str]] = {g: [] for g in ("HD", "D", "C", "P", "F")}
    for g, lst in groups.items():
        for raw in lst:
            s = admin.summarize_student(raw)
            by_grade[g].append(_fmt_name_grade_mark(s))
    for g in ("HD", "D", "C", "P", "F"):
        inside = ", ".join(by_grade[g])
        print(f"{g}  --> [{inside}]")

def _print_pass_fail(admin: AdminSubsystem) -> None:
    _print_header("PASS/FAIL Partition", S.CY)
    pf = {"FAIL": [], "PASS": []}
    for bucket, lst in admin.categorise_pass_fail().items():
        for raw in lst:
            s = admin.summarize_student(raw)
            pf[bucket].append(_fmt_name_grade_mark(s))
    print(f"FAIL --> [{', '.join(pf['FAIL'])}]")
    print(f"PASS --> [{', '.join(pf['PASS'])}]")

def _print_cohort_stats(admin: AdminSubsystem) -> None:
    groups = admin.organise_by_grade()
    count = sum(len(v) for v in groups.values())
    pass_count = len(admin.categorise_pass_fail().get("PASS", []))
    pass_rate = (pass_count / count) if count else 0.0
    dist = {g: len(groups.get(g, [])) for g in ("HD", "D", "C", "P", "F")}
    _print_header("Cohort Stats", S.CY)
    print(f"Total students: {count}")
    print(f"Pass rate: {pass_rate:.2%}")
    print(f"Grade distribution: {dist}")

def _clear_database_flow(admin: AdminSubsystem) -> None:
    _print_header("Clearing students database", S.YL)
    ans = input("Are you sure you want to clear the database (Y)ES/(N)O: ").strip().upper()
    if ans != "Y":
        print(f"{S.RD}Cancelled.{S.R}")
        return
    admin.clear_students()
    print(f"{S.GR}Students data cleared{S.R}")