import tkinter as tk
from gui_elements.draggable import make_draggable

def create_spinbox(parent, select_callback=None):
    spn = tk.Spinbox(parent, from_=0, to=10)
    spn.place(x=550, y=100, width=80)
    make_draggable(spn, select_callback)
    return spn
