# cli/main.py
# cli/main.py 的文件顶部
from controllers.student_subsystem import StudentSubsystem

# ...  class System  ...
class System:
    def __init__(self):
        
        self.student_subsystem = StudentSubsystem() 
        pass

    # 1. Main Menu Method: startCLI() - University Menu
    def startCLI(self):
        while True:
            print("\n==================================")
            print("  Welcome to University App CLI")
            print("==================================")
            print("A: Admin System")    # <--- Navigate to Admin Menu
            print("S: Student System")  # <--- Navigate to Student Menu
            print("X: Exit Application")
            print("----------------------------------")

            # .strip().upper() ensures clean input regardless of case or whitespace
            choice = input("Enter your choice: ").strip().upper()

            if choice == 'A':
                # Required navigation for Admin Menu (Ved's task)
                self.admin_system_menu()

            elif choice == 'S':
                # Call the student sub-menu method
                self.student_system_menu()

            elif choice == 'X':
                print("Exiting University Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter A, S, or X.")

# 2. Student Sub-Menu Method: student_system_menu() (Suzy's main focus)
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
                
                result = self.student_subsystem.login(email, password)
                
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
                
                result = self.student_subsystem.register(name, email, password)
                print(result["message"])
                
            elif choice == 'X':
                break  # Returns to the main startCLI() loop

            else:
                print("Invalid choice. Please enter L, R, or X.")

    # 3. Admin Placeholder Method: admin_system_menu()
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

    # 4. 新增方法：学生登录后的主面板 (使用 Snake Case 规范)
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
                # 🚨 Snake Case 调用: enrol_subject
                self.student_subsystem.enrol_subject(subject_name)

            elif choice == 'C':
                new_pass = input("Enter new password: ")
                confirm_pass = input("Confirm new password: ")
                # 🚨 Snake Case 调用: change_password
                self.student_subsystem.change_password(new_pass, confirm_pass)
                
            elif choice == 'V':
                # 🚨 Snake Case 调用: view_enrolments
                enrolments = self.student_subsystem.view_enrolments()
                print(f"Current Enrolments: {enrolments}")
                
            elif choice == 'L':
                # 登出后返回初始 Student System Menu
                self.student_subsystem.logout()
                break 

            else:
                print("Invalid choice. Please try again.")

# Application entry point (starts the CLI when main.py is run directly)
if __name__ == "__main__":
    app = System()
    app.startCLI()
 