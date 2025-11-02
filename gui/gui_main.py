# gui/gui_main.py (Conflict Resolved Version)

import tkinter as tk
from tkinter import messagebox
from .login_frame import LoginFrame
from .enrol_frame import EnrolmentFrame # Assuming this is the correct name
from .subject_frame import SubjectFrame
from controllers.student_subsystem import StudentSubsystem

class GUIUniApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("University Student App")
        self.geometry("600x400")  # Window size (optional)
        
        # 确保只实例化一次 StudentSubsystem
        self.student_subsystem = StudentSubsystem()  
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        # --- Add frames ---
        # 整合您和团队的界面框架
        for F in (LoginFrame, EnrolmentFrame, SubjectFrame): 
            page_name = F.__name__
            # 将 subsystem 实例传递给每个框架
            frame = F(parent=container, app=self, subsystem=self.student_subsystem)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginFrame")  # Start with LoginFrame

    def show_frame(self, page_name):
        """Display the frame corresponding to the given page name."""
        frame = self.frames[page_name]
        frame.tkraise()
        # Refresh data when switching to EnrolmentFrame
        if page_name == "EnrolmentFrame":
            # Assuming EnrolmentFrame has a method to refresh data
            # frame.refresh_data() 
            pass 
            
    def on_login_success(self, student):
        """Called after a successful login to switch to the EnrolmentFrame."""
        # 登录成功后切换到选课界面
        self.show_frame("EnrolmentFrame")


# --- Run the application ---
if __name__ == "__main__":
    # StudentSubsystem 已经在 GUIUniApp 的 __init__ 中实例化，此处无需重复
    app = GUIUniApp()
    app.mainloop()