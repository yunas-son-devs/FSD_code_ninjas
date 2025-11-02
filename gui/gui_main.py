from .login_frame import LoginFrame
from .enrol_frame import EnrolmentFrame
from .subject_frame import SubjectFrame
from .exception_frame import ExceptionWindow
import tkinter as tk
from controllers.student_subsystem import StudentSubsystem

class GUIUniApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("University Student App")
        self.geometry("600x400")  # Window size (optional)
        
        self.student_subsystem = StudentSubsystem()  # Keep subsystem naming consistent
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        # --- Add frames ---
        for F in (LoginFrame, EnrolmentFrame):  # Add future frames here as well
            page_name = F.__name__
            frame = F(parent=container, app=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginFrame")  # Start with LoginFrame

    def show_frame(self, page_name):
        """Display the frame corresponding to the given page name."""
        frame = self.frames[page_name]
        frame.tkraise()
        # Refresh data when switching to EnrolmentFrame
        if page_name == "EnrolmentFrame":
            frame.refresh_data() 
            
    def on_login_success(self, student):
        """Called after a successful login to switch to the EnrolmentFrame."""
        # The student object is already stored in subsystem.current_student,
        # so we can switch frames and let the frame handle data refresh.
        self.show_frame("EnrolmentFrame")


# --- Run the application ---
if __name__ == "__main__":
    app = GUIUniApp()
    app.mainloop()
