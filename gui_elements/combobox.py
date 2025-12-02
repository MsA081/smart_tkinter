import tkinter as tk
from tkinter import ttk
from gui_elements.draggable import make_draggable

def create_combobox(parent, select_callback=None):
    combo = ttk.Combobox(parent, values=["Option 1", "Option 2", "Option 3"])
    combo.place(x=400, y=100, width=150)
    make_draggable(combo, select_callback)
    return combo
