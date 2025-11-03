# cli/main.py
from controllers.student_subsystem import StudentSubsystem
from .login_cli import student_login, student_register
from .enrol_cli import subject_menu
from .admin_cli import admin_menu

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
                admin_menu()
            elif choice == 'S':
                self.student_system_menu()
            elif choice == 'X':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

    def student_system_menu(self):
        while True:
            print("\n--- Student System Menu ---")
            print("L: Login")      
            print("R: Register")
            print("X: Return to Main Menu")
            print("---------------------------")

            choice = input("Enter your choice: ").strip().upper()

            if choice == 'L':
                email = input("Enter student email: ").strip()
                password = input("Enter password: ").strip()
                result = self.subsystem.login(email, password)
                
                if isinstance(result, dict):
                    if result.get("success"):
                        print(result["message"])
                        self.student_logged_in_menu()
                    else:
                        print(result["message"])
                elif result:
                    print("Login successful!")
                    self.student_logged_in_menu()
                else:
                    print("Login failed.")

            elif choice == 'R':
                name = input("Enter student name: ").strip()
                email = input("Enter student email: ").strip()
                password = input("Enter password: ").strip()
                result = self.subsystem.register(name, email, password)

                if isinstance(result, dict):
                    print(result["message"])
                elif result:
                    print("Registration successful!")
                else:
                    print("Registration failed.")
                    
            elif choice == 'X':
                break
            else:
                print("Invalid choice.")
    
    def admin_system_menu(self):
        while True:
            print("\n--- Admin System Menu ---")
            print("X: Return to Main Menu")
            choice = input("Enter your choice: ").strip().upper()
            if choice == 'X':
                break
            else:
                print("Invalid choice.")

    def student_logged_in_menu(self):
        while True:
            print("\n--- Student Dashboard ---")
            print("E: Enrol Subject")
            print("V: View Enrolments")
            print("C: Change Password")
            print("L: Logout")
            print("-------------------------")
            
            choice = input("Enter your choice: ").strip().upper()

            if choice == 'E':
                subject_name = input("Enter subject name: ")
                self.subsystem.enrol_subject(subject_name)
            elif choice == 'C':
                new_pass = input("Enter new password: ")
                confirm_pass = input("Confirm password: ")
                self.subsystem.change_password(new_pass, confirm_pass)
            elif choice == 'V':
                enrolments = self.subsystem.view_enrolments()
                print(f"Enrolments: {enrolments}")
            elif choice == 'L':
                self.subsystem.logout()
                break 
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    app = System()
    app.start_cli()
