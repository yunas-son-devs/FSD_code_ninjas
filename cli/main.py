# cli/main.py
from controllers.student_subsystem import StudentSubsystem
from .login_cli import student_login, student_register
from .enrol_cli import subject_menu
#from .admin_cli import admin_menu

class System:
    def __init__(self):
        self.subsystem = StudentSubsystem()

    def start_cli(self):
        while True:
            print("\n=== University CLI ===")
            print("A: Admin System")
            print("S: Student System")
            print("X: Exit")
            choice = input("Enter choice: ").strip().upper()

            if choice == 'A':
                print("Please implement admin_menu Ved")
                # admin_menu(self.subsystem)
            elif choice == 'S':
                self.student_system_menu()
            elif choice == 'X':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

<<<<<<< HEAD
    def student_system_menu(self):
        while True:
            print("\n--- Student Menu ---")
            print("L: Login")
            print("R: Register")
            print("X: Back to Main Menu")
            choice = input("Enter choice: ").strip().upper()

            if choice == 'L':
                if student_login(self.subsystem):
                    subject_menu(self.subsystem)
            elif choice == 'R':
                student_register(self.subsystem)
=======
    # 2. Student System Menu
    def student_system_menu(self):
        while True:
            print("\n--- Student System Menu ---")
            print("L: Login")
            print("R: Register")
            print("X: Return to Main Menu")
            print("---------------------------")

            choice = input("Enter your choice: ").strip().upper()

            if choice == 'L':
                # -------------------- Login --------------------
                print("\n=== Student Login ===")
                email = input("Enter your email: ").strip()
                password = input("Enter your password: ").strip()
                self.student_subsystem.login(email, password)

            elif choice == 'R':
                # -------------------- Register --------------------
                print("\n=== Student Registration ===")
                name = input("Enter your name: ").strip()
                email = input("Enter your email: ").strip()
                password = input("Enter your password: ").strip()
                self.student_subsystem.register(name, email, password)

>>>>>>> feature/gui
            elif choice == 'X':
                break
            else:
                print("Invalid choice.")

<<<<<<< HEAD
=======
    # 3. Admin System Menu (placeholder)
    def admin_system_menu(self):
        while True:
            print("\n--- Admin System Menu (Ved's Task Placeholder) ---")
            print("X: Return to Main Menu")
            print("--------------------------------------------------")
            choice = input("Enter your choice: ").strip().upper()

            if choice == 'X':
                break
            else:
                print("Invalid choice. Please enter X.")

# Application entry point (starts the CLI when main.py is run directly)
>>>>>>> feature/gui
if __name__ == "__main__":
    app = System()
    app.start_cli()
