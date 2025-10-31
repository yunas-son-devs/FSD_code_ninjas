from controllers.data_manager import DataManager
from controllers.student_subsystem import StudentSubsystem
from models.student import Student

# create a fresh student each run
st = Student(id=Student.generateStudentID(), name="Vipin", email="vipin@uni.com", password="Abc12345")
ss = StudentSubsystem(st)

# --- Enrol 2 subjects (this should auto-save after each enrol) ---
s1 = ss.enrolSubject("FSD")
s2 = ss.enrolSubject("DB")
print("Before reload:", len(st.subjects), "subjects;", "avg =", st.average_mark, "status =", st.pass_fail)

# --- Explicit save (optional, your auto-save already did it) ---
DataManager.saveData([st])

# --- Reload from disk and verify ---
students = DataManager.loadData()
reloaded = students[0]
print("After reload:", len(reloaded.subjects), "subjects;", "avg =", reloaded.average_mark, "status =", reloaded.pass_fail)

# --- Remove one subject by ID (auto-saves again) ---
removed = ss.removeSubject(s1.id)
print("Removed first subject?", removed)

# --- Reload again to verify persistence of removal ---
students2 = DataManager.loadData()
reloaded2 = students2[0]
print("After removal & reload:", len(reloaded2.subjects), "subjects;", "avg =", reloaded2.average_mark, "status =", reloaded2.pass_fail)
print("IDs now:", [s.id for s in reloaded2.subjects])

