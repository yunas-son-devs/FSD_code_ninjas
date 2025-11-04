from controllers.student_subsystem import StudentSubsystem
# --- robust colorama import (works even if metadata is weird) ---
try:
    import colorama
    colorama.init(autoreset=True)
    Fore = colorama.Fore
    Style = colorama.Style
except Exception:
    class _Fore: RED = GREEN = CYAN = YELLOW = ""
    class _Style: RESET_ALL = ""
    Fore, Style = _Fore(), _Style()
# ----------------------------------------------------------------



def student_login(subsystem: StudentSubsystem):
    print(Fore.CYAN + "\n=== Student Login ===")
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

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
    password = input("Enter your password: ").strip()

    if subsystem.register(name, email, password):
        print(Fore.GREEN + "Registration successful!")
    else:
        print(Fore.RED + "Registration failed. Try again.")
