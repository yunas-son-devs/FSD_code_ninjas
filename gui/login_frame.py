# gui/login_frame.py
import tkinter as tk
from tkinter import messagebox as mb
from tkinter.simpledialog import askstring

class LoginFrame(tk.Frame):
    """
    Login Window GUI
    - Email / Password Widget
    - Login / Register Button
    - Calls StudentSubsystem methods
    """
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.subsystem = app.student_subsystem 
        self.place(relwidth=1, relheight=1)

        # Email
        tk.Label(self, text="Email").pack(pady=(20, 0))
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=(0, 10))

        # Password
        tk.Label(self, text="Password").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=(0, 10))

        # Login
        tk.Button(self, text="Login", width=15, command=self.login).pack(pady=(5, 5))

        # Register
        tk.Button(self, text="Register", width=15, command=self.register).pack(pady=(5, 20))

    def login(self):
        """Call StudentSubsystem login + Success/Failure popup"""
        email = self.email_entry.get()
        password = self.password_entry.get()
        if self.subsystem.login(email, password):
            mb.showinfo("Login Successful", f"Welcome {self.subsystem.current_student.name}")
            self.app.on_login_success(self.subsystem.current_student) 
        else:
            mb.showerror("Login Error", "Incorrect email or password")

    def register(self):
        """Call StudentSubsystem register + Success/Failure popup"""
        name = askstring("Register", "Enter your name")
        email = askstring("Register", "Enter your email")
        password = askstring("Register", "Enter your password")

        if not (name and email and password):
            mb.showerror("Error", "All fields are required")
            return

        if self.subsystem.register(name, email, password):
            mb.showinfo("Success", "Registration successful")
        else:
            mb.showerror("Error", "Registration failed")
