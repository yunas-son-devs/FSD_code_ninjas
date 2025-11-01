# cli/enrol_cli.py
from controllers.student_subsystem import StudentSubsystem

def subject_menu(subsystem: StudentSubsystem):
    if not subsystem.current_student:
        print("No student logged in.")
        return

    while True:
        print("\n--- Subject Enrolment Menu ---")
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
                print("Password changed successfully.")
            else:
                print("Password change failed. Please try again.")

        elif choice == 'e':
            subject_name = f"Subject {len(subsystem.current_student.subjects) + 1}"
            
            # Check if max subjects reached before calling enrol
            if len(subsystem.current_student.subjects) >= subsystem.MAX_SUBJECTS:
                print(f"Cannot enrol: Maximum of {subsystem.MAX_SUBJECTS} subjects reached.")
                continue

            # Enrolling with a generated subject name. ID, mark, and grade are generated in StudentSubsystem.enrol_subject.
            if subsystem.enrol_subject(subject_name):
                print(f"Successfully enrolled in a new subject: '{subject_name}'. ID, Mark, and Grade assigned automatically.")
            else:
                # The enrol_subject method already prints a specific error if max subjects is reached or already enrolled.
                pass

        elif choice == 'r':
            subjects = subsystem.view_enrolments()
            if not subjects:
                print("No subjects enrolled.")
                continue

            while True:
                print("\nEnrolled subjects:")
                # Including subject ID in the printout for easier reference/removal
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
                            print(f"Subject '{subjects[idx - 1]['name']}' removed successfully.")
                            subjects = subsystem.view_enrolments() # Refresh list after removal
                        else:
                            print("Removal failed. Try again.")
                        break
                    else:
                        print("Invalid number. Please enter a valid subject number.")
                except ValueError:
                    print("Invalid input. Please enter a number corresponding to a subject.")

        elif choice == 's':
            subjects = subsystem.view_enrolments()
            if not subjects:
                print("No subjects enrolled.")
            else:
                print("\nYour enrolled subjects:")
                for sub in subjects:
                    # --- MODIFIED VIEW LOGIC: ADDED SUBJECT ID ---
                    print(f"ID: {sub['id']} -> {sub['name']} - Mark: {sub['mark']:.2f}, Grade: {sub['grade']}")
                    # --- END MODIFIED VIEW LOGIC ---

        elif choice == 'x':
            break

        else:
            print("Invalid choice. Please enter one of the menu options.")
