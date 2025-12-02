import tkinter as tk
from gui_elements.draggable import make_draggable

def create_radiobutton(parent, select_callback=None):
    var = tk.IntVar()
    rbtn = tk.Radiobutton(parent, text="Option 1", variable=var, value=1, bg="white", fg="black")
    rbtn.place(x=350, y=100)
    make_draggable(rbtn, select_callback)
    return rbtn
