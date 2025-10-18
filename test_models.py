from models.subject import Subject
from models.student import Student

# --- Test Subject ---
sub = Subject(id=Subject.generateSubjectID(), name="FSD")
sub.assign_mark()
sub.calculate_grade()
print("Subject:", sub.id, sub.name, sub.mark, sub.grade)

# --- Test Student ---
st = Student(id=Student.generateStudentID(), name="Vipin", email="vipin@uni.com", password="Test123")
print("Student ID:", st.id)
print("Has max subjects?", st.hasMaxSubjects())

# Enrol 4 subjects and test again
for n in ["FSD", "DB", "NET", "SE"]:
    s = Subject(id=Subject.generateSubjectID(), name=n)
    s.assign_mark(); s.calculate_grade()
    st.subjects.append(s)

print("Total subjects:", len(st.subjects))
print("Has max subjects now?", st.hasMaxSubjects())
