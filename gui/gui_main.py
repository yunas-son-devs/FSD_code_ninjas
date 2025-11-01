# gui/gui_main.py (수정된 전체 구조)
import tkinter as tk
from controllers.student_subsystem import StudentSubsystem
# ------------------ Import Frames ------------------
from .login_frame import LoginFrame 
from .enrol_frame import EnrolmentFrame # <-- 새 프레임 import

class GUIUniApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("University Student App")
        self.geometry("600x400") # 창 크기 설정 (옵션)
        
        self.student_subsystem = StudentSubsystem() # subsystem 이름을 통일합니다.
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        # --- 프레임 추가 ---
        for F in (LoginFrame, EnrolmentFrame): # 앞으로 만들 프레임도 여기에 추가합니다.
            page_name = F.__name__
            frame = F(parent=container, app=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginFrame") # 시작은 LoginFrame

    def show_frame(self, page_name):
        """Show a frame for the given page name."""
        frame = self.frames[page_name]
        frame.tkraise()
        # EnrolmentFrame으로 전환 시 데이터를 새로고침합니다.
        if page_name == "EnrolmentFrame":
            frame.refresh_data() 
            
    def on_login_success(self, student):
        """로그인 성공 시 호출되어 EnrolmentFrame으로 전환합니다."""
        # student 객체는 이미 subsystem.current_student에 저장되어 있으므로,
        # 바로 프레임 전환을 호출하고 데이터 새로고침을 위임합니다.
        self.show_frame("EnrolmentFrame")


# --- Run the Application ---
if __name__ == "__main__":
    app = GUIUniApp()
    app.mainloop()