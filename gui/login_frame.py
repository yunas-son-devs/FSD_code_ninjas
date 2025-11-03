import tkinter as tk
from tkinter import messagebox as mb
from tkinter.simpledialog import askstring

class LoginFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.subsystem = app.student_subsystem
        self.place(relwidth=1, relheight=1)

        tk.Label(self, text="Email").pack(pady=(12, 2))
        self.email_entry = tk.Entry(self, width=32)
        self.email_entry.pack(pady=2)

        tk.Label(self, text="Password").pack(pady=(8, 2))
        self.password_entry = tk.Entry(self, width=32)
        self.password_entry.pack(pady=2)

        row = tk.Frame(self)
        row.pack(pady=10)
        tk.Button(row, text="Login", width=12, command=self.login).pack(side="left", padx=4)
        tk.Button(row, text="Register", width=12, command=self.register).pack(side="left", padx=4)
        tk.Button(row, text="Admin", width=10, command=self.admin_access).pack(side="left", padx=4)

        self.email_entry.bind("<Return>", lambda _e: self.login())
        self.password_entry.bind("<Return>", lambda _e: self.login())
        self.email_entry.focus_set()

    def _get_name(self, s):
        return s.get("name") if isinstance(s, dict) else getattr(s, "name", "student")

    def login(self):
        email = (self.email_entry.get() or "").strip()
        password = (self.password_entry.get() or "").strip()
        if self.subsystem.login(email, password):
            s = self.subsystem.current_student
            mb.showinfo("Login Successful", f"Welcome {self._get_name(s)}")
            self.app.on_login_success(s)
        else:
            mb.showerror(title="Login Error", message="Incorrect email or password")

    def register(self):
        name = askstring("Register", "Enter your name")
        if not name:
            return
        email = askstring("Register", "Enter your email")
        if not email:
            return
        password = askstring("Register", "Enter your password")
        if not password:
            return
        if self.subsystem.register(name, email, password):
            mb.showinfo("Success", "Registration successful")
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, email)
            self.password_entry.delete(0, tk.END)
        else:
            mb.showerror("Error", "Registration failed")

    def admin_access(self):
        pw = askstring("Admin Access", "Enter admin password:", show="*")
        if pw == "Abcde123":
            self.app.open_admin()
        else:
            mb.showerror("Admin Access", "Incorrect admin password")