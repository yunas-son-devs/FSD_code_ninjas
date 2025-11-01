# cli/main.py
# cli/main.py 的文件顶部
from controllers.student_subsystem import StudentSubsystem
from colorama import init, Fore, Style
init(autoreset=True)

# ...  class System  ...
class System:
    def __init__(self):
        
        self.student_subsystem = StudentSubsystem(current_student=None)

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
                print(Fore.GREEN + "Exiting University Application. Goodbye!")

                break
            else:
                print(Fore.RED + "Invalid choice. Please enter A, S, or X.")


    # 2. Student Sub-Menu Method: student_system_menu() (Suzy's main focus)
    def student_system_menu(self):
        while True:
            print("\n--- Student System Menu ---")
            print("L: Login")      # <-- Week 2 Logic
            print("R: Register")   # <-- Week 2 Logic
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
                break  # Returns to the main startCLI() loop

            else:
                print(Fore.RED + "Invalid choice. Please enter L, R, or X.")


    # 3. Admin Placeholder Method: admin_system_menu() (Fulfills navigation requirement)
    def admin_system_menu(self):
        while True:
            print("\n--- Admin System Menu (Ved's Task Placeholder) ---")
            print("X: Return to Main Menu")
            print("--------------------------------------------------")
            
            choice = input("Enter your choice: ").strip().upper()
            
            if choice == 'X':
                break  # Returns to the main startCLI() loop
            else:
                print(Fore.RED + "Invalid choice. Please enter X.")


# Application entry point (starts the CLI when main.py is run directly)
if __name__ == "__main__":
    app = System()
    app.startCLI()