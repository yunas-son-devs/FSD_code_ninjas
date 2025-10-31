# gui/gui_main.py
import tkinter as tk
from tkinter import messagebox
from controllers.student_subsystem import StudentSubsystem
from controllers.data_manager import DataManager
from models.student import Student

class StudentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Enrolment System")
        self.root.geometry("520x480")

        # load or create one student
        students = DataManager.loadData()
        self.student = students[0] if students else Student(
            id=Student.generateStudentID(), name="Vipin",
            email="vipin@uni.com", password="Abc12345"
        )
        self.ss = StudentSubsystem(self.student)

        tk.Label(root, text="Enter Subject (name or ID):").pack(pady=6)
        self.entry = tk.Entry(root, width=40)
        self.entry.pack()

        tk.Button(root, text="Enrol Subject", command=self.enrol).pack(pady=4)
        tk.Button(root, text="Remove by Subject ID", command=self.remove).pack(pady=4)
        tk.Button(root, text="View Enrolments", command=self.view).pack(pady=4)
        tk.Button(root, text="Exit & Save", command=self.exit).pack(pady=10)

        self.out = tk.Text(root, width=64, height=18)
        self.out.pack()

    def enrol(self):
        name = self.entry.get().strip()
        if not name:
            messagebox.showwarning("Input", "Enter a subject name.")
            return
        try:
            sub = self.ss.enrolSubject(name)
            self.out.insert(tk.END, f"Enrolled: {sub.id} {sub.name} {sub.mark} {sub.grade}\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def remove(self):
        sid = self.entry.get().strip()
        if not sid:
            messagebox.showwarning("Input", "Enter Subject ID to remove.")
            return
        ok = self.ss.removeSubject(sid)
        self.out.insert(tk.END, "Removed.\n" if ok else "ID not found.\n")

    def view(self):
        self.out.delete(1.0, tk.END)
        for s in self.ss.viewEnrolments():
            self.out.insert(tk.END, f"{s['id']} - {s['name']} ({s['mark']}, {s['grade']})\n")

    def exit(self):
        DataManager.saveData([self.student])
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    StudentGUI(root)
    root.mainloop()
