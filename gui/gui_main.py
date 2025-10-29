import tkinter as tk
from login_frame import LoginFrame
from enrol_frame import EnrolFrame
from subject_frame import SubjectFrame

class GUIUniApp(tk.Tk):
    def __init__(self, student_subsystem):
        super().__init__()
        self.title("GUIUniApp")
        self.geometry("400x300")
        self.student_subsystem = student_subsystem
        self.current_frame = None
        self.show_login()

    def show_frame(self, frame_class, *args):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self, *args)
        self.current_frame.pack(fill="both", expand=True)

    def show_login(self):
        self.show_frame(LoginFrame, self.on_login_success)

    def show_enrol(self):
        self.show_frame(EnrolFrame, self.on_subject_action)

    def show_subject(self):
        self.show_frame(SubjectFrame, self.on_subject_action)

    # Callbacks
    def on_login_success(self, student):
        # student: logged-in student object
        self.show_enrol()

    def on_subject_action(self, action, subject):
        # action: "enrol" or "remove"
        # subject: selected subject details
        print(f"Action: {action}, Subject: {subject}")


if __name__ == "__main__":
    from controllers.student_subsystem import StudentSubsystem

    # StudentSubsystem 객체 생성
    subsystem = StudentSubsystem()

    # GUI 실행
    app = GUIUniApp(subsystem)
    app.mainloop()  # mainloop() 호출
