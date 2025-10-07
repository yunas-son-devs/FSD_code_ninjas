# cli/main.py

class System:
    def __init__(self):
        # 暂时留空，后续用于初始化 Subsystem 实例
        pass

    # 1. 主菜单方法：startCLI() - University Menu
    def startCLI(self):
        while True:
            print("\n==================================")
            print("  Welcome to University App CLI")
            print("==================================")
            print("A: Admin System")    # <--- 跳转到 Admin 菜单
            print("S: Student System")  # <--- 跳转到 Student 菜单
            print("X: Exit Application")
            print("----------------------------------")

            # .strip().upper() 用于规范化输入
            choice = input("Enter your choice: ").strip().upper()

            if choice == 'A':
                # 任务要求：实现 Admin 菜单导航
                self.admin_system_menu()

            elif choice == 'S':
                # 调用您的学生子菜单方法
                self.student_system_menu()

            elif choice == 'X':
                print("Exiting University Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter A, S, or X.")

    # 2. 学生子菜单方法：student_system_menu() (Suzy 的主要菜单)
    def student_system_menu(self):
        while True:
            print("\n--- Student System Menu ---")
            print("L: Login")      # <-- Week 2 逻辑
            print("R: Register")   # <-- Week 2 逻辑
            print("X: Return to Main Menu")
            print("---------------------------")

            choice = input("Enter your choice: ").strip().upper()

            if choice == 'L':
                print("Login selected. (Your Week 2 Task: StudentSubsystem.login())")
                # self.student_subsystem.login_prompt()

            elif choice == 'R':
                print("Register selected. (Your Week 2 Task: StudentSubsystem.register())")
                # self.student_subsystem.register_prompt()

            elif choice == 'X':
                break  # 返回到 startCLI() 中的主循环

            else:
                print("Invalid choice. Please enter L, R, or X.")

    # 3. Admin 占位符方法：admin_system_menu() (满足导航要求)
    def admin_system_menu(self):
        while True:
            print("\n--- Admin System Menu (Ved's Task) ---")
            print("X: Return to Main Menu")
            print("--------------------------------------")