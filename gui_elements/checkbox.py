import tkinter as tk
from gui_elements.draggable import make_draggable

def create_checkbox(parent, select_callback=None):
    var = tk.BooleanVar()
    chk = tk.Checkbutton(parent, text="Check Me", variable=var, bg="white", fg="black")
    chk.place(x=300, y=100)
    make_draggable(chk, select_callback)
    return chk
