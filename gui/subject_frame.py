import tkinter as tk
from exception_frame import ExceptionWindow

class SubjectFrame(tk.Frame):
    def __init__(self, master, action_callback):
        super().__init__(master)
        self.action_callback = action_callback

        tk.Label(self, text="My Subjects").pack()
        self.subject_listbox = tk.Listbox(self)
        # TODO: Bring actual subjects from StudentSubsystem
        for sub in ["Math"]:  # dummy
            self.subject_listbox.insert(tk.END, sub)
        self.subject_listbox.pack()

        tk.Button(self, text="Remove", command=self.remove_subject).pack()
        tk.Button(self, text="Back to Enrol", command=master.show_enrol).pack()

    def remove_subject(self):
        try:
            selection = self.subject_listbox.curselection()
            if not selection:
                raise Exception("No subject selected")
            subject = self.subject_listbox.get(selection[0])
            self.action_callback("remove", subject)
        except Exception as e:
            ExceptionWindow(self.master, str(e))
