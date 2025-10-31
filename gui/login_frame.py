import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import messagebox as mb
from controllers.student_subsystem import StudentSubsystem

class LoginFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.subsystem = app.student_subsystem
        self.place(relwidth=1, relheight=1)

        tk.Label(self, text="Email").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.login).pack()
        tk.Button(self, text="Register", command=self.register).pack()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if self.subsystem.login(email, password):
          mb.showinfo("Login Successful", f"Welcome {self.subsystem.current_student.name}")
        # Show enrolment frame upon successful login
          self.app.on_login_success(self.subsystem.current_student)
        # self.app.show_enrol() 
        else:
          mb.showerror(title="Login Error", message="Incorrect email or password")


    def register(self):
        # Use popup dialogs to get registration info
        from tkinter.simpledialog import askstring
        name = askstring("Register", "Enter your name")
        email = askstring("Register", "Enter your email")
        password = askstring("Register", "Enter your password")
        if self.subsystem.register(name, email, password):
            mb.showinfo("Success", "Registration successful")
        else:
            mb.showerror("Error", "Registration failed")
