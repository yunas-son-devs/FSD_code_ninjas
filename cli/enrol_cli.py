# cli/enrol_cli.py
from controllers.student_subsystem import StudentSubsystem
from colorama import Fore, init

init(autoreset=True)

def subject_menu(subsystem: StudentSubsystem):
    if not subsystem.current_student:
        print(Fore.RED + "No student logged in.")
        return

    while True:
        print(Fore.CYAN + "\n--- Subject Enrolment Menu ---")
        print("(c) Change password")
        print("(e) Enrol in a subject (max 4)")
        print("(r) Remove a subject")
        print("(s) Show enrolled subjects")
        print("(x) Exit to Student Menu")
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'c':
            new_pw = input("New password: ").strip()
            confirm_pw = input("Confirm password: ").strip()
            if subsystem.change_password(new_pw, confirm_pw):
                print(Fore.GREEN + "Password changed successfully.")
            else:
                print(Fore.RED + "Password change failed. Please try again.")

        elif choice == 'e':
            subject_name = f"Subject {len(subsystem.current_student.subjects) + 1}"
            
            if len(subsystem.current_student.subjects) >= subsystem.MAX_SUBJECTS:
                print(Fore.RED + f"Cannot enrol: Maximum of {subsystem.MAX_SUBJECTS} subjects reached.")
                continue

            if subsystem.enrol_subject(subject_name):
                print(Fore.GREEN + f"Successfully enrolled in '{subject_name}'. ID, Mark, and Grade assigned automatically.")
            else:
                print(Fore.RED + "Enrolment failed. Try again.")

        elif choice == 'r':
            subjects = subsystem.view_enrolments()
            if not subjects:
                print(Fore.RED + "No subjects enrolled.")
                continue

            while True:
                print(Fore.CYAN + "\nEnrolled subjects:")
                for i, sub in enumerate(subjects, 1):
                    print(f"{i}. {sub['name']} (ID: {sub['id']})")
                
                user_input = input("Enter the subject number to remove (or 'x' to cancel): ").strip()

                if user_input.lower() == 'x':
                    break

                try:
                    idx = int(user_input)
                    if 1 <= idx <= len(subjects):
                        removed = subsystem.remove_subject(subjects[idx - 1]["id"])
                        if removed:
                            print(Fore.GREEN + f"Subject '{subjects[idx - 1]['name']}' removed successfully.")
                            subjects = subsystem.view_enrolments()
                        else:
                            print(Fore.RED + "Removal failed. Try again.")
                        break
                    else:
                        print(Fore.RED + "Invalid number. Please enter a valid subject number.")
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a number corresponding to a subject.")

        elif choice == 's':
            subjects = subsystem.view_enrolments()
            if not subjects:
                print(Fore.RED + "No subjects enrolled.")
            else:
                print(Fore.CYAN + "\nYour enrolled subjects:")
                for sub in subjects:
                    print(f"ID: {sub['id']} -> {sub['name']} - Mark: {sub['mark']:.2f}, Grade: {sub['grade']}")

        elif choice == 'x':
            print(Fore.YELLOW + "Returning to Student Menu...")
            break

        else:
            print(Fore.RED + "Invalid choice. Please enter one of the menu options.")
