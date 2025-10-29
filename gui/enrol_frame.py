import tkinter as tk
from exception_frame import ExceptionWindow

class EnrolFrame(tk.Frame):
    def __init__(self, master, enrol_callback):
        super().__init__(master)
        self.enrol_callback = enrol_callback

        tk.Label(self, text="Available Subjects").pack()
        self.subject_listbox = tk.Listbox(self)
        # TODO: Bring actual subjects from StudentSubsystem
        for sub in ["Math", "Physics", "CS"]:
            self.subject_listbox.insert(tk.END, sub)
        self.subject_listbox.pack()

        tk.Button(self, text="Enrol", command=self.enrol_subject).pack()
        tk.Button(self, text="Go to My Subjects", command=master.show_subject).pack()

    def enrol_subject(self):
        try:
            selection = self.subject_listbox.curselection()
            if not selection:
                raise Exception("No subject selected")
            subject = self.subject_listbox.get(selection[0])
            self.enrol_callback("enrol", subject)
        except Exception as e:
            ExceptionWindow(self.master, str(e))
