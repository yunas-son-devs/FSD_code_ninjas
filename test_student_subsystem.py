from models.student import Student
from controllers.student_subsystem import StudentSubsystem

# Create a dummy student (normally comes from login/DB)
st = Student(id=Student.generateStudentID(), name="Vipin", email="vipin@uni.com", password="Abc12345")
ss = StudentSubsystem(current_student=st)

print("Start:", st.name, st.id, "subjects =", len(st.subjects), "avg =", st.average_mark, st.pass_fail)

# Enrol 4 subjects
for n in ["FSD", "DB", "NET", "SE"]:
    sub = ss.enrolSubject(n)
    print("Enrolled:", sub.id, sub.name, sub.mark, sub.grade)

print("After enrol:", len(st.subjects), "avg =", st.average_mark, "status =", st.pass_fail)

# Try to enrol 5th (should error)
try:
    ss.enrolSubject("Fifth")
except Exception as e:
    print("Expected error:", e)

# View list
print("View:", ss.viewEnrolments())

# Remove one
to_remove = st.subjects[0].id
ok = ss.removeSubject(to_remove)
print("Removed?", ok, "Now count:", len(st.subjects), "avg =", st.average_mark, "status =", st.pass_fail)

# Change password
try:
    ss.changePassword("NewPass123", "NewPass123")
    print("Password changed OK")
except Exception as e:
    print("Password change failed:", e)
