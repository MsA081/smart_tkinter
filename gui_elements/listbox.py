import tkinter as tk
from gui_elements.draggable import make_draggable

def create_listbox(parent, select_callback=None):
    lst = tk.Listbox(parent, bg="white", fg="black", font=("Segoe UI", 10), width=20, height=5)
    lst.insert(0, "Item 1")
    lst.insert(1, "Item 2")
    lst.insert(2, "Item 3")
    lst.place(x=450, y=100)
    make_draggable(lst, select_callback)
    return lst
