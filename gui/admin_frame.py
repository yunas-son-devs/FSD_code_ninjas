# gui/admin_frame.py
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
from controllers.admin_subsystem import AdminSubsystem

class AdminFrame(tk.Frame):
    def __init__(self, parent, admin=None, on_close=None):
        super().__init__(parent)
        self.on_close = on_close
        self.admin = admin or AdminSubsystem()

        toolbar = tk.Frame(self)
        toolbar.pack(fill="x", pady=6, padx=6)

        tk.Button(toolbar, text="Refresh", command=self.refresh).pack(side="left", padx=4)
        tk.Button(toolbar, text="View selected", command=self.view_selected).pack(side="left", padx=4)
        tk.Button(toolbar, text="Remove selected", command=self.remove_selected).pack(side="left", padx=4)
        tk.Button(toolbar, text="Back to Login", command=self._back).pack(side="right", padx=4)

        columns = ("id", "name", "email", "nsubj", "avg")
        self.table = ttk.Treeview(self, columns=columns, show="headings", height=12)
        self.table.pack(fill="both", expand=True, padx=6, pady=(0,6))

        self.table.heading("id", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("email", text="Email")
        self.table.heading("nsubj", text="# Subj")
        self.table.heading("avg", text="Average")

        self.table.column("id", width=90, anchor="w")
        self.table.column("name", width=140, anchor="w")
        self.table.column("email", width=250, anchor="w")
        self.table.column("nsubj", width=60, anchor="e")
        self.table.column("avg", width=80, anchor="e")

        self.status = tk.Label(self, anchor="w")
        self.status.pack(fill="x", padx=6, pady=(0,6))

        self.refresh()

    def _get(self, obj, key, default=None):
        return obj.get(key, default) if isinstance(obj, dict) else getattr(obj, key, default)

    def _subjects(self, s):
        return self._get(s, "subjects") or self._get(s, "enrolments") or []

    def _avg(self, s):
        v = self._get(s, "averageMark")
        if isinstance(v, (int, float)):
            return float(v)
        marks = []
        for sub in self._subjects(s):
            mark = sub.get("mark") if isinstance(sub, dict) else getattr(sub, "mark", None)
            if isinstance(mark, (int, float)):
                marks.append(mark)
        return sum(marks) / len(marks) if marks else 0.0

    def refresh(self):
        for i in self.table.get_children():
            self.table.delete(i)
        students = self.admin.view_all_students() or []
        for s in students:
            sid = str(self._get(s, "id") or self._get(s, "studentID") or "")
            name = self._get(s, "name", "")
            email = self._get(s, "email", "")
            nsubj = len(self._subjects(s))
            avg = f"{self._avg(s):.2f}"
            self.table.insert("", "end", iid=sid, values=(sid, name, email, nsubj, avg))
        self.status.config(text=f"Total: {len(students)}")

    def view_selected(self):
        sel = self.table.selection()
        if not sel:
            mb.showerror("View", "Select a student first.")
            return
        sid = sel[0]
        students = self.admin.view_all_students()
        found = None
        for s in students:
            if str(self._get(s, "id") or self._get(s, "studentID") or "") == sid:
                found = s
                break
        if not found:
            mb.showerror("View", f"Student {sid} not found.")
            return

        win = tk.Toplevel(self)
        win.title("Student details")

        info = tk.Frame(win)
        info.pack(fill="x", padx=10, pady=8)

        name = self._get(found, "name", "")
        email = self._get(found, "email", "")
        avg = f"{self._avg(found):.2f}"
        grade = self._get(found, "grade") or self._get(found, "overallGrade") or ""
        pf = self._get(found, "passFailStatus") or self._get(found, "status") or ""

        tk.Label(info, text=f"ID: {sid}").grid(row=0, column=0, sticky="w", padx=4)
        tk.Label(info, text=f"Name: {name}").grid(row=0, column=1, sticky="w", padx=12)
        tk.Label(info, text=f"Email: {email}").grid(row=1, column=0, columnspan=2, sticky="w", padx=4, pady=(4,0))
        tk.Label(info, text=f"Average: {avg}").grid(row=2, column=0, sticky="w", padx=4, pady=(4,0))
        tk.Label(info, text=f"Grade: {grade}").grid(row=2, column=1, sticky="w", padx=12, pady=(4,0))
        tk.Label(info, text=f"Pass/Fail: {pf}").grid(row=2, column=2, sticky="w", padx=12, pady=(4,0))

        cols = ("code", "name", "mark", "grade")
        tv = ttk.Treeview(win, columns=cols, show="headings", height=10)
        tv.pack(fill="both", expand=True, padx=10, pady=8)
        for c, lab, w, anc in [
            ("code", "Code", 90, "w"),
            ("name", "Name", 220, "w"),
            ("mark", "Mark", 80, "e"),
            ("grade", "Grade", 80, "center"),
        ]:
            tv.heading(c, text=lab)
            tv.column(c, width=w, anchor=anc)

        for sub in self._subjects(found):
            code = sub.get("code") if isinstance(sub, dict) else getattr(sub, "code", "")
            nm = sub.get("name") if isinstance(sub, dict) else getattr(sub, "name", "")
            mk = sub.get("mark") if isinstance(sub, dict) else getattr(sub, "mark", "")
            gr = sub.get("grade") if isinstance(sub, dict) else getattr(sub, "grade", "")
            tv.insert("", "end", values=(code, nm, mk, gr))

        tk.Button(win, text="Close", command=win.destroy).pack(pady=(0,10))

    def remove_selected(self):
        sel = self.table.selection()
        if not sel:
            mb.showerror("Remove", "Select a student first.")
            return
        sid = sel[0]
        ok, msg = self.admin.remove_student(sid)
        if ok:
            mb.showinfo("Remove", msg)
            self.refresh()
        else:
            mb.showerror("Remove", msg)

    def _back(self):
        if self.on_close:
            self.on_close()
            