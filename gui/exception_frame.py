import tkinter as tk
from tkinter import messagebox

class ExceptionWindow:
    def __init__(self, master, message):
        messagebox.showerror("Error", message)