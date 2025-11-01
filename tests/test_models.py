from models.subject import Subject
from models.student import Student

# --- Test Subject ---
sub = Subject(id=Subject.generate_subject_id(), name="FSD")
sub.assign_mark()
sub.calculate_grade()
print("Subject:", sub.id, sub.name, sub.mark, sub.grade)

# --- Test Student ---
st = Student(id=Student.generate_student_id(), name="Vipin", email="vipin@uni.com", password="Test123")
print("Student ID:", st.id)
print("Has max subjects?", st.has_max_subjects())

# Enrol 4 subjects and test again
for n in ["FSD", "DB", "NET", "SE"]:
    s = Subject(id=Subject.generate_subject_id(), name=n)
    s.assign_mark(); s.calculate_grade()
    st.subjects.append(s)

print("Total subjects:", len(st.subjects))
print("Has max subjects now?", st.has_max_subjects())
