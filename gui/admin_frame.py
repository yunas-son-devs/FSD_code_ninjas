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
        tk.Button(toolbar, text="Grade Grouping", command=self.show_grade_groups).pack(side="left", padx=6)
        tk.Button(toolbar, text="PASS/FAIL", command=self.show_pass_fail).pack(side="left", padx=4)
        tk.Button(toolbar, text="Cohort Stats", command=self.show_stats).pack(side="left", padx=4)
        tk.Button(toolbar, text="Clear DB", command=self.clear_db).pack(side="left", padx=6)
        tk.Button(toolbar, text="Back to Login", command=self._back).pack(side="right", padx=4)

        columns = ("id", "name", "email")
        self.table = ttk.Treeview(self, columns=columns, show="headings", height=16)
        self.table.pack(fill="both", expand=True, padx=6, pady=(0,6))
        self.table.heading("id", text="Student ID")
        self.table.heading("name", text="Name")
        self.table.heading("email", text="Email ID")
        self.table.column("id", width=160, anchor="w")
        self.table.column("name", width=220, anchor="w")
        self.table.column("email", width=360, anchor="w")

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

    def _grade(self, s):
        g = self._get(s, "grade") or self._get(s, "overallGrade")
        if isinstance(g, str) and g in {"HD", "D", "C", "P", "F"}:
            return g
        avg = self._avg(s)
        if avg >= 85: return "HD"
        if avg >= 75: return "D"
        if avg >= 65: return "C"
        if avg >= 50: return "P"
        return "F"

    def _pass_fail(self, s):
        pf = self._get(s, "passFailStatus") or self._get(s, "status")
        if isinstance(pf, str) and pf.upper() in {"PASS", "FAIL"}:
            return pf.upper()
        return "PASS" if self._avg(s) >= 50 else "FAIL"

    def _subject_pf(self, sub):
        val = sub.get("passFail") if isinstance(sub, dict) else getattr(sub, "passFail", None)
        if isinstance(val, str) and val.upper() in {"PASS", "FAIL"}:
            return val.upper()
        m = sub.get("mark") if isinstance(sub, dict) else getattr(sub, "mark", None)
        return "PASS" if isinstance(m, (int, float)) and m >= 50 else "FAIL"

    def refresh(self):
        for i in self.table.get_children():
            self.table.delete(i)
        students = self.admin.view_all_students() or []
        for s in students:
            sid = str(self._get(s, "id") or self._get(s, "studentID") or "")
            name = self._get(s, "name", "")
            email = self._get(s, "email", "")
            self.table.insert("", "end", iid=sid, values=(sid, name, email))
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
        win.geometry("880x520")

        info = tk.Frame(win)
        info.pack(fill="x", padx=10, pady=8)

        name = self._get(found, "name", "")
        email = self._get(found, "email", "")
        avg = f"{self._avg(found):.2f}"
        grade = self._grade(found)
        pf = self._pass_fail(found)
        nsubj = len(self._subjects(found))

        tk.Label(info, text=f"Student ID: {sid}").grid(row=0, column=0, sticky="w", padx=4)
        tk.Label(info, text=f"Name: {name}").grid(row=0, column=1, sticky="w", padx=12)
        tk.Label(info, text=f"Email ID: {email}").grid(row=1, column=0, columnspan=2, sticky="w", padx=4, pady=(4,0))
        tk.Label(info, text=f"Average: {avg}").grid(row=2, column=0, sticky="w", padx=4, pady=(4,0))
        tk.Label(info, text=f"Grade: {grade}").grid(row=2, column=1, sticky="w", padx=12, pady=(4,0))
        tk.Label(info, text=f"Pass/Fail: {pf}").grid(row=2, column=2, sticky="w", padx=12, pady=(4,0))
        tk.Label(info, text=f"Subjects Count: {nsubj}").grid(row=3, column=0, sticky="w", padx=4, pady=(4,0))

        cols = ("sid", "name", "mark", "grade", "pf")
        tv = ttk.Treeview(win, columns=cols, show="headings", height=14)
        tv.pack(fill="both", expand=True, padx=10, pady=8)
        for c, lab, w, anc in [
            ("sid", "Subject ID", 140, "w"),
            ("name", "Subject Name", 360, "w"),
            ("mark", "Marks", 100, "e"),
            ("grade", "Grade", 100, "center"),
            ("pf", "Pass/Fail", 100, "center"),
        ]:
            tv.heading(c, text=lab)
            tv.column(c, width=w, anchor=anc)

        for sub in self._subjects(found):
            sub_id = sub.get("id") if isinstance(sub, dict) else getattr(sub, "id", "")
            nm = sub.get("name") if isinstance(sub, dict) else getattr(sub, "name", "")
            mk = sub.get("mark") if isinstance(sub, dict) else getattr(sub, "mark", "")
            gr = sub.get("grade") if isinstance(sub, dict) else getattr(sub, "grade", "")
            pf_s = self._subject_pf(sub)
            tv.insert("", "end", values=(sub_id, nm, mk, gr, pf_s))

        tk.Button(win, text="Close", command=win.destroy).pack(pady=(0,10))

    def remove_selected(self):
        sel = self.table.selection()
        if not sel:
            mb.showerror("Remove", "Select a student first.")
            return
        sid = sel[0]
        if not mb.askyesno("Remove", f"Remove student {sid}?"):
            return
        ok, msg = self.admin.remove_student(sid)
        if ok:
            mb.showinfo("Remove", msg)
            self.refresh()
        else:
            mb.showerror("Remove", msg)

    def show_grade_groups(self):
        groups = self.admin.organise_by_grade()
        win = tk.Toplevel(self)
        win.title("Grade Grouping")
        win.geometry("880x520")
        txt = tk.Text(win, width=100, height=26)
        txt.pack(fill="both", expand=True)
        for g in ("HD", "D", "C", "P", "F"):
            line = []
            for s in groups.get(g, []):
                sid = str(self._get(s, "id") or self._get(s, "studentID") or "")
                nm = self._get(s, "name", "")
                avg = f"{self._avg(s):.2f}"
                line.append(f"{nm}::{sid}  GRADE:{g}  AVG:{avg}")
            txt.insert("end", f"{g} --> [{';  '.join(line)}]\n")
        txt.config(state="disabled")

    def show_pass_fail(self):
        buckets = self.admin.categorise_pass_fail()
        win = tk.Toplevel(self)
        win.title("PASS / FAIL")
        win.geometry("880x520")
        txt = tk.Text(win, width=100, height=26)
        txt.pack(fill="both", expand=True)
        for key in ("FAIL", "PASS"):
            line = []
            for s in buckets.get(key, []):
                sid = str(self._get(s, "id") or self._get(s, "studentID") or "")
                nm = self._get(s, "name", "")
                avg = f"{self._avg(s):.2f}"
                gr = self._grade(s)
                line.append(f"{nm}::{sid}  GRADE:{gr}  AVG:{avg}")
            txt.insert("end", f"{key} --> [{';  '.join(line)}]\n")
        txt.config(state="disabled")

    def show_stats(self):
        groups = self.admin.organise_by_grade()
        total = sum(len(v) for v in groups.values())
        pass_count = len(self.admin.categorise_pass_fail().get("PASS", []))
        pass_rate = (pass_count / total) if total else 0.0
        dist = {g: len(groups.get(g, [])) for g in ("HD", "D", "C", "P", "F")}
        mb.showinfo(
            "Cohort Stats",
            f"Total students: {total}\n"
            f"Pass rate: {pass_rate:.2%}\n"
            f"Grade distribution: {dist}"
        )

    def clear_db(self):
        if not mb.askyesno("Clear Database", "Are you sure you want to clear all students?"):
            return
        self.admin.clear_students()
        mb.showinfo("Clear Database", "Students data cleared.")
        self.refresh()

    def _back(self):
        if self.on_close:
            self.on_close()