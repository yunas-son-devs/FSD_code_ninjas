# gui/enrol_frame.py
import tkinter as tk
from tkinter import messagebox as mb
from tkinter.simpledialog import askstring
from controllers.student_subsystem import StudentSubsystem
from models.subject import Subject
from .exception_frame import ExceptionWindow

class EnrolmentFrame(tk.Frame):
    """
    GUI for Subject Enrolment
    - Displays enrolled subjects, student summary, and core functions.
    """
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.subsystem: StudentSubsystem = app.student_subsystem 
        self.place(relwidth=1, relheight=1)
        
        # Variables to store UI components
        self.summary_label = None
        self.subject_listbox = None 
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container (for layout)
        main_container = tk.Frame(self)
        main_container.pack(pady=20, padx=20, fill="both", expand=True)

        # 1. Student summary section
        self.summary_label = tk.Label(
            main_container,
            text="Student Summary",
            font=("Arial", 12, "bold"),
            justify=tk.LEFT
        )
        self.summary_label.pack(fill="x", pady=(0, 10))

        # 2. Subjects list section
        tk.Label(main_container, text="Enrolled Subjects (Max 4):").pack(pady=(10, 5), anchor="w")
        
        list_frame = tk.Frame(main_container)
        list_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        self.subject_listbox = tk.Listbox(list_frame, height=8, font=("Courier", 10))
        self.subject_listbox.pack(side="left", fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.subject_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.subject_listbox.config(yscrollcommand=scrollbar.set)

        # 3. Buttons section
        button_frame = tk.Frame(main_container)
        button_frame.pack(fill="x", pady=10)
        
        # Enrol Button
        tk.Button(button_frame, text="Enrol New Subject", command=self.enrol_subject).pack(side="left", padx=5)
        
        # Remove Button
        tk.Button(button_frame, text="Remove Selected Subject", command=self.remove_subject).pack(side="left", padx=5)
        
        # Change Password Button
        tk.Button(button_frame, text="Change Password", command=self.change_password).pack(side="left", padx=5)

        # Logout Button
        tk.Button(main_container, text="Logout", command=self.logout).pack(pady=(10, 0))


    def refresh_data(self):
        """Update student summary and subject list when called."""
        student = self.subsystem.current_student
        if not student:
            return

        # 1. Update summary info
        summary = (
            f"ID: {student.id} | Name: {student.name} | Email: {student.email}\n"
            f"Avg Mark: {student.average_mark:.2f} | Status: {student.pass_fail}"
        )
        self.summary_label.config(text=summary)

        # 2. Update subject list
        self.subject_listbox.delete(0, tk.END)
        self.subject_listbox.insert(tk.END, "ID    | Name                                | Mark | Grade")
        self.subject_listbox.insert(tk.END, "------|-------------------------------------|------|------")
        
        subjects = self.subsystem.view_enrolments()
        for s in subjects:
            line = (
                f"{s['id']:<5} | {s['name']:<35} | {s['mark']:<4.2f} | {s['grade']}"
            )
            self.subject_listbox.insert(tk.END, line)

    # ------------------ Action Methods ------------------
    
    def enrol_subject(self):
        """Automatically generate a subject name and enrol the student."""
        student = self.subsystem.current_student

        # --- Debug output ---
        print("DEBUG: current_student type:", type(student))
        print("DEBUG: current_student dir:", dir(student))
        # ----------------------

        if student.has_max_subjects():
            mb.showerror("Enrolment Error", f"Maximum of {student.MAX_SUBJECTS} subjects reached.")
            return

        # Generate a subject name
        subject_name = f"Subject {len(student.subjects) + 1}"

        if self.subsystem.enrol_subject(subject_name):
            mb.showinfo("Success", f"Successfully enrolled in: '{subject_name}'")
        else:
            mb.showerror("Error", "Enrolment failed. Check console for details.")
            
        self.refresh_data()


    def remove_subject(self):
        """Remove the subject selected in the listbox."""
        selection = self.subject_listbox.curselection()
        if not selection or selection[0] < 2:
            mb.showerror("Error", "Please select a subject (not a header) to remove.")
            return
        
        # Extract Subject ID from the listbox line
        selected_line = self.subject_listbox.get(selection[0])
        subject_id = selected_line.split('|')[0].strip()
        
        if mb.askyesno("Confirm Removal", f"Are you sure you want to remove Subject ID: {subject_id}?"):
            if self.subsystem.remove_subject(subject_id):
                mb.showinfo("Success", f"Subject {subject_id} removed.")
            else:
                mb.showerror("Error", "Removal failed. Subject ID not found.")
        
        self.refresh_data()


    def change_password(self):
        """Handle the Change Password workflow using simpledialog."""
        new_pw = askstring("Change Password", "Enter new password:", parent=self)
        if not new_pw:
            return

        confirm_pw = askstring("Change Password", "Confirm new password:", parent=self)
        if not confirm_pw:
            return

        # StudentSubsystem.change_password handles validation and saving
        if self.subsystem.change_password(new_pw, confirm_pw):
            mb.showinfo("Success", "Password changed successfully.")
        else:
            mb.showerror("Error", "Password change failed. Check validation rules or mismatch.")


    def logout(self):
        """Call StudentSubsystem logout and switch back to LoginFrame."""
        if self.subsystem.logout():
            mb.showinfo("Logout", "Logout successful. Goodbye!")
            self.app.show_frame("LoginFrame")
        else:
            mb.showerror("Error", "Logout failed.")
