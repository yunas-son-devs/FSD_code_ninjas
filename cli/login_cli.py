# cli/login_cli.py
from controllers.student_subsystem import StudentSubsystem

def student_login(subsystem: StudentSubsystem):
    print("\n=== Student Login ===")
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    if subsystem.login(email, password):
        print(f"Login successful! Welcome {subsystem.current_student.name}")
        return True
    else:
        print("Login failed. Check your email or password.")
        return False

def student_register(subsystem: StudentSubsystem):
    print("\n=== Student Registration ===")
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()
    if subsystem.register(name, email, password):
        print("Registration successful!")
    else:
        print("Registration failed. Try again.")
