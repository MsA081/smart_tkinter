from tkinter import ttk
from gui_elements.draggable import make_draggable

def create_progressbar(parent, select_callback=None):
    pbar = ttk.Progressbar(parent, orient="horizontal", length=150, mode="determinate")
    pbar.place(x=650, y=100)
    pbar["value"] = 50
    make_draggable(pbar, select_callback)
    return pbar
