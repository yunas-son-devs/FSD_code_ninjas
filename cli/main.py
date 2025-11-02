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
                
                # 兼容两种返回值类型
                if isinstance(result, dict):
                    if result.get("success"):
                        print(result["message"])
                        # 登录成功后，跳转到新的学生主面板
                        self.student_logged_in_menu()
                    else:
                        print(result["message"]) # 打印失败原因
                elif result:
                    print("Login successful!")
                    self.student_logged_in_menu()
                else:
                    print("Login failed.")

            elif choice == 'R':
                # --- 实际的注册流程 ---
                name = input("Enter student name: ").strip()
                email = input("Enter student email: ").strip()
                password = input("Enter password: ").strip()

                result = self.subsystem.register(name, email, password)

                # 兼容两种返回值类型
                if isinstance(result, dict):
                    # 返回字典（你之前的版本）
                    print(result["message"])
                elif result:
                    # 返回 True（main 分支的版本）
                    print("Registration successful!")
                else:
                    # 返回 False
                    print("Registration fa