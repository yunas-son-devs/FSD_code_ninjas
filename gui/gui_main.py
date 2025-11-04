from .login_frame import LoginFrame
from .enrol_frame import EnrolmentFrame
from .admin_frame import AdminFrame
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
from controllers.student_subsystem import StudentSubsystem

ADMIN_PASSWORD = "Abcde123"

class GUIUniApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("University Student App")
        self.geometry("900x520")
        self.student_subsystem = StudentSubsystem()
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (LoginFrame, EnrolmentFrame):
            page_name = F.__name__
            frame = F(parent=container, app=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.admin_frame = None
        self.container = container
        self.show_frame("LoginFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "EnrolmentFrame":
            frame.refresh_data()

    def on_login_success(self, student):
        self.show_frame("EnrolmentFrame")

    def open_admin(self):
        pwd = sd.askstring("Admin Login", "Enter admin password:")
        if pwd is None:
            return
        if pwd != ADMIN_PASSWORD:
            mb.showerror("Admin Login", "Access denied.")
            return
        if self.admin_frame is None:
            self.admin_frame = AdminFrame(
                parent=self.container,
                admin=None,
                on_close=lambda: self.show_frame("LoginFrame"),
            )
            self.admin_frame.grid(row=0, column=0, sticky="nsew")
        self.admin_frame.refresh()
        self.admin_frame.tkraise()


if __name__ == "__main__":
    app = GUIUniApp()
    app.mainloop()