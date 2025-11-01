from controllers.student_subsystem import StudentSubsystem
from colorama import Fore, init
import maskpass

init(autoreset=True)


def student_login(subsystem: StudentSubsystem):
    print(Fore.CYAN + "\n=== Student Login ===")
    email = input("Enter your email: ").strip()
    password = maskpass.askpass("Enter your password: ", mask="*").strip()

    if subsystem.login(email, password):
        print(Fore.GREEN + f"Login successful! Welcome {subsystem.current_student.name}")
        return True
    else:
        print(Fore.RED + "Login failed. Check your email or password.")
        return False


def student_register(subsystem: StudentSubsystem):
    print(Fore.CYAN + "\n=== Student Registration ===")
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    password = maskpass.askpass("Enter your password: ", mask="*").strip()

    if subsystem.register(name, email, password):
        print(Fore.GREEN + "Registration successful!")
    else:
        print(Fore.RED + "Registration failed. Try again.")
