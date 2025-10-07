# cli/main.py

class System:
    def __init__(self):
        # 团队其他成员的 Subsystem 类，后续使用
        # self.admin_subsystem = AdminSubsystem()
        # self.student_subsystem = StudentSubsystem()
        pass

    # 1. 主菜单方法：startCLI()
    def startCLI(self):
        while True:
            print("\n==================================")
            print("  Welcome to University App CLI")
            print("==================================")
            print("A: Admin System")
            print("S: Student System")  # <-- 进入学生菜单
            print("X: Exit Application")
            print("----------------------------------")

            # .strip().upper() 用于规范化输入
            choice = input("Enter your choice: ").strip().upper()

            if choice == 'A':
                print("Entering Admin System... (Ved's task)")
                # self.admin_subsystem.start_menu()

            elif choice == 'S':
                # 调用您的学生子菜单方法
                self.student_system_menu()

            elif choice == 'X':
                print("Exiting University Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter A, S, or X.")

    # 2. 学生子菜单方法：student_system_menu()
    def student_system_menu(self):
        while True:
            print("\n--- Student System Menu ---")
            print("L: Login")      # <-- 登录选项
            print("R: Register")   # <-- 注册选项
            print("X: Return to Main Menu")
            print("---------------------------")

            choice = input("Enter your choice: ").strip().upper()

            if choice == 'L':
                print("Login selected. (Your Week 2 Task)")
                # self.student_subsystem.login_prompt()

            elif choice == 'R':
                print("Register selected. (Your Week 2 Task)")
                # self.student_subsystem.register_prompt()

            elif choice == 'X':
                break  # 返回到 startCLI() 中的主循环

            else:
                print("Invalid choice. Please enter L, R, or X.")


# 程序运行的入口
if __name__ == "__main__":
    app = System()
    app.startCLI()