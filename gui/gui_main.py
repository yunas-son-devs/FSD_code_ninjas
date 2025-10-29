# gui/gui_main.py (Temporary Working Skeleton for Integration)

import tkinter as tk
from tkinter import messagebox

# 导入您的 StudentSubsystem 类 (假设路径正确)
from controllers.student_subsystem import StudentSubsystem 

class GUI_App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("University App Login")
        self.geometry("300x200")

        # 实例化您的 StudentSubsystem
        self.student_subsystem = StudentSubsystem()

        # --- 假设的输入字段 ---
        # 实际中 Yuna 会提供这些，但我们现在用占位符
        self.email_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self, show="*")
        
        tk.Label(self, text="Email:").pack()
        self.email_entry.pack()
        tk.Label(self, text="Password:").pack()
        self.password_entry.pack()

        # --- 登录按钮 (挂载事件处理函数) ---
        self.login_button = tk.Button(
            self, 
            text="Login", 
            command=self.handle_login_click # <--- 按钮点击时调用这个函数
        )
        self.login_button.pack(pady=10)

    # --- 您的事件处理函数和逻辑 ---
    
    # 1. 按钮点击事件处理函数
    def handle_login_click(self):
        # A. 从 GUI 界面获取输入值
        email = self.email_entry.get()
        password = self.password_entry.get()

        # B. 调用您的 StudentSubsystem 登录逻辑
        result = self.student_subsystem.login(email, password)

        # C. 根据返回结果显示弹窗
        if result["success"]:
            # 成功
            messagebox.showinfo("Login Success", result["message"])
            self.switch_to_dashboard() # 假设成功后跳转到主界面
        else:
            # 失败
            messagebox.showerror("Login Failed", result["message"])

    # 2. 占位符函数（用于测试流程）
    def switch_to_dashboard(self):
        # 模拟成功登录后要做的事情
        print("Login Successful. Now switching to the main application dashboard (placeholder).")
        # 通常会销毁当前窗口或切换框架
        self.destroy() 


# 程序启动入口
if __name__ == "__main__":
    app = GUI_App()
    app.mainloop()