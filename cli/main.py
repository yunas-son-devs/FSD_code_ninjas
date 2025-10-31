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

            elif choice == 'X':
                break
            else:
                print("Invalid choice. Please enter L, R, or X.")

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
if __name__ == "__main__":
    app = System()
    app.startCLI()