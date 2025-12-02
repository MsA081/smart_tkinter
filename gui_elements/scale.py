import tkinter as tk
from gui_elements.draggable import make_draggable

def create_scale(parent, select_callback=None):
    scl = tk.Scale(parent, from_=0, to=100, orient="horizontal")
    scl.set(50)
    scl.place(x=500, y=100, width=150)
    make_draggable(scl, select_callback)
    return scl
