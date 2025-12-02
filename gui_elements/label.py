import tkinter as tk
from gui_elements.draggable import make_draggable

def create_label(parent, select_callback=None):
    lbl = tk.Label(parent, text="Label", bg="lightgray", fg="black")
    lbl.place(x=150, y=100)
    make_draggable(lbl, select_callback)
    return lbl
