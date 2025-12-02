from tkinter import ttk

def apply_theme(root):
    style = ttk.Style(root)
    style.theme_use("default")

    style.configure("TButton", font=("Segoe UI", 10), padding=5)
    style.configure("TLabel", font=("Segoe UI", 10))
    style.configure("TEntry", font=("Segoe UI", 10))
    style.configure("TCombobox", font=("Segoe UI", 10))
    style.configure("TCheckbutton", font=("Segoe UI", 10))
    style.configure("TRadiobutton", font=("Segoe UI", 10))
    style.configure("TProgressbar", thickness=10)
