# controllers/student_subsystem.py

# --- Dependencies from teammates (Assumed to be in the 'main' branch) ---
from utils.validator import Validator      # Yuna's validation tools
from controllers.data_manager import DataManager  # Ved's data persistence tools
from models.student import Student         # Vipin's Student model structure


class StudentSubsystem:
    def __init__(self):
        self.data_manager = DataManager()
        # Load all student data from the file system on subsystem initialization
        # Assumes DataManager.loadData() returns a list of Student objects
        self.all_students = self.data_manager.loadData() 
        self.current_student = None  # Tracks the currently logged-in student

    # --- Core Method: Registration ---
    def register(self, name, email, password):
        # 1. Input Validation (Depends on Yuna's Validator)
        
        # Check email format
        if not Validator.validateEmail(email):
            print("Registration failed: Invalid email format.")
            return False

        # Check password strength and format
        if not Validator.validatePassword(password):
            # The print message should align with Validator's feedback
            print("Registration failed: Password does not meet security requirements.")
            return False

        # 2. Existence Check (Preventing duplicate registration)
        for student_obj in self.all_students:
            # Check if the email is already registered (case-insensitive)
            if student_obj.email.lower() == email.lower():
                print("Registration failed: This email is already registered.")
                return False

        # 3. Create New Student Object (Depends on Yuna's ID generator and Vipin's Model)
        
        # Get a unique ID (Depends on Yuna's Validator)
        student_id = Validator.generateStudentID() 

        # Create a new Student instance (Depends on Vipin's Student model)
        try:
            # Assumes Student constructor is Student(id, name, email, password)
            new_student = Student(student_id, name, email, password)
        except Exception as e:
            print(f"Error creating student object: {e}")
            return False
        
        # 4. Data Persistence (Depends on Ved's DataManager)
        self.all_students.append(new_student) 

        # Save the updated list to the file system (Depends on Ved's DataManager)
        if self.data_manager.saveData(self.all_students):
            print(f"Registration successful! Student ID: {student_id}")
            return True
        else:
            # Rollback: Remove the object from memory if file save failed
            self.all_students.pop() 
            print("Registration failed: Could not save data to file.")
            return False

    # --- Core Method: Login ---
    def login(self, email, password):
        # 1. Find the User
        target_student = None
        for student_obj in self.all_students:
            # Find user by email (case-insensitive)
            if student_obj.email.lower() == email.lower():
                target_student = student_obj
                break
        
        if target_student is None:
            print("Login failed: User not found.")
            return False

        # 2. Password Verification
        # Assumes password stored in the model is the plain text string
        if target_student.password == password:
            # 3. Login Success
            self.current_student = target_student  # Set the current session
            print(f"Login successful! Welcome, {target_student.name}.")
            return True
        else:
            # Incorrect password
            print("Login failed: Incorrect password.")
            return False

    # --- Core Method: Logout ---
    def logout(self):
        if self.current_student is not None:
            student_name = self.current_student.name
            self.current_student = None  # Clear the current student session
            print(f"Logout successful. Goodbye, {student_name}.")
            return True
        else:
            print("Error: No user is currently logged in.")
            return False

# NOTE: No 'if __name__ == "__main__":' block needed here, 
# as this file is intended to be imported as a module by cli/main.py.