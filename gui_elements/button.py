import tkinter as tk
from gui_elements.draggable import make_draggable

def create_button(parent, select_callback=None):
    btn = tk.Button(parent, text="Click Me", bg="lightblue")
    btn.place(x=100, y=100)
    make_draggable(btn, select_callback)
    return btn
