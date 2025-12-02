import tkinter as tk
from gui_elements.draggable import make_draggable

def create_canvas(parent, select_callback=None):
    cvs = tk.Canvas(parent, width=200, height=150, bg="lightyellow", highlightthickness=1, highlightbackground="gray")
    cvs.create_rectangle(20, 20, 100, 100, fill="blue")
    cvs.place(x=600, y=100)
    make_draggable(cvs, select_callback)
    return cvs
