import tkinter as tk
from tkinter import ttk
from gui_elements.draggable import make_draggable

def create_notebook(parent, select_callback=None):
    nb = ttk.Notebook(parent)
    frame1 = tk.Frame(nb, bg="white")
    frame2 = tk.Frame(nb, bg="white")
    nb.add(frame1, text="Tab 1")
    nb.add(frame2, text="Tab 2")
    nb.place(x=700, y=100, width=200, height=100)
    make_draggable(nb, select_callback)
    return nb
