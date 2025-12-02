import tkinter as tk
from gui_elements.draggable import make_draggable

def create_textbox(parent, select_callback=None):
    txt = tk.Text(parent, width=30, height=5, bg="white", fg="black")
    txt.place(x=250, y=100)
    make_draggable(txt, select_callback)
    return txt
