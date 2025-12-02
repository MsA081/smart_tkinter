import tkinter as tk
from PIL import Image, ImageTk
from gui_elements.draggable import make_draggable
import os

def create_image(parent, select_callback=None):
    image_path = "assets/sample.png"
    if os.path.exists(image_path):
        img = Image.open(image_path).resize((100, 100))
        photo = ImageTk.PhotoImage(img)
        lbl = tk.Label(parent, image=photo)
        lbl.image = photo  # نگه داشتن مرجع برای جلوگیری از پاک شدن تصویر
    else:
        lbl = tk.Label(parent, text="Image not found", bg="red")

    lbl.place(x=100, y=400)
    make_draggable(lbl, select_callback)
    return lbl
