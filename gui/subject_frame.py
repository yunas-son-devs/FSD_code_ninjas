import tkinter as tk
from .exception_frame import ExceptionWindow 

class SubjectFrame(tk.Frame):
    def __init__(self, master, action_callback):
        super().__init__(master)
        self.action_callback = action_callback

        tk.Label(self, text="My Subjects").pack()
        self.subject_listbox = tk.Listbox(self)
        self.subject_listbox.pack()

        # Display actual subjects
        self.refresh_subject_list()

        tk.Button(self, text="Remove", command=self.remove_subject).pack()
        tk.Button(self, text="Back to Enrol", command=master.show_enrol).pack()

    def refresh_subject_list(self):
        self.subject_listbox.delete(0, tk.END)
        if self.master.subsystem.current_student:
            for sub in self.master.subsystem.current_student.subjects:
                self.subject_listbox.insert(tk.END, sub.name)

    def remove_subject(self):
        try:
            selection = self.subject_listbox.curselection()
            if not selection:
                raise Exception("No subject selected")
            subject_name = self.subject_listbox.get(selection[0])

            # Find actual Subject object
            sub_obj = next(
                (s for s in self.master.subsystem.current_student.subjects if s.name == subject_name),
                None
            )
            if not sub_obj:
                raise Exception("Subject not found")

            if self.action_callback("remove", sub_obj.id):
                self.refresh_subject_list()
        except Exception as e:
            ExceptionWindow(self.master, str(e))
