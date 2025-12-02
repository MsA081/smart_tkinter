import tkinter as tk
from gui_elements.draggable import make_draggable

def create_entry(parent, select_callback=None):
    ent = tk.Entry(parent, bg="white", fg="black")
    ent.place(x=200, y=100, width=150)
    make_draggable(ent, select_callback)
    return ent
