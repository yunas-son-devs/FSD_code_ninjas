# cli/main.py
from controllers.student_subsystem import StudentSubsystem
from .login_cli import student_login, student_register
from .enrol_cli import subject_menu
from .admin_cli import admin_menu

class System:
    def __init__(self):
        # 确保 student_subsystem 实例名称为 subsystem
        self.subsystem = StudentSubsystem() 

    def start_cli(self):
        while True:
            print("\n=== University CLI ===")
            print("A: Admin System")
            print("S: Student System")
            print("X: Exit")
            choice = input("Enter choice: ").strip().upper()

            if choice == 'A':
                admin_menu() # Ved/Team's Admin Menu Call

            elif choice == 'S':
                self.student_system_menu()
            elif choice == 'X':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

    # --- Student System Menu (Login/Register) ---
    def student_system_menu(self):
        while True:
            print("\n--- Student System Menu ---")
            print("L: Login")      
            print("R: Register")
            print("X: Return to Main Menu")
            print("---------------------------")

            choice = input("Enter your choice: ").strip().upper()

            if choice == 'L':
                # --- 实际的登录流程 ---
                email = input("Enter student email: ").strip()
                password = input("Enter password: ").strip()
                
                result = self.subsystem.login(email, password)
                
                if result.get("success"):
                    print(result["message"])
                    # 登录成功后，跳转到新的学生主面板
                    self.student_logged_in_menu()
                else:
                    print(result["message"]) # 打印失败原因

            elif choice == 'R':
                # --- 实际的注册流程 ---
                name = input("Enter student name: ").strip()
                email = input("Enter student email: ").strip()
                password = input("Enter password: ").strip()
                
                result = self.subsystem.register(name, email, password)
                print(result["message"])
                
            elif choice == 'X':
                break
            else:
                print("Invalid choice.")
    
    # --- Admin Placeholder (Kept for compatibility) ---
    def admin_system_menu(self):
        # 实际代码已被 Ved 替代，此处保留兼容性。
        while True:
            print("\n--- Admin System Menu (Ved's Task Placeholder) ---")
            print("X: Return to Main Menu")
            print("--------------------------------------------------")
            
            choice = input("Enter your choice: ").strip().upper()
            
            if choice == 'X':
                break
            else:
                print("Invalid choice. Please enter X.")

    # --- Student Logged-In Menu (Your Logic) ---
    def student_logged_in_menu(self):
        while True:
            print("\n--- Student Dashboard (Logged In) ---")
            print("E: Enrol Subject")
            print("V: View Enrolments")
            print("C: Change Password")
            print("L: Logout")
            print("-------------------------------------")
            
            choice = input("Enter your choice: ").strip().upper()

            if choice == 'E':
                subject_name = input("Enter subject name to enrol: ")
                # 使用 snake_case: enrol_subject
                self.subsystem.enrol_subject(subject_name)

            elif choice == 'C':
                new_pass = input("Enter new password: ")
                confirm_pass = input("Confirm new password: ")
                # 使用 snake_case: change_password
                self.subsystem.change_password(new_pass, confirm_pass)
                
            elif choice == 'V':
                # 使用 snake_case: view_enrolments
                enrolments = self.subsystem.view_enrolments()
                print(f"Current Enrolments: {enrolments}")
                
            elif choice == 'L':
                self.subsystem.logout()
                break 

            else:
                print("Invalid choice. Please try again.")

# Application entry point (starts the CLI when main.py is run directly)
if __name__ == "__main__":
    app = System()
    app.start_cli()