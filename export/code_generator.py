import json
import os

CONFIG_PATH = "assets/config.json"

def save_layout(frames):
    layout = []
    for i, frame in enumerate(frames):
        page = []
        for w in frame.winfo_children():
            widget_info = {
                "type": w.winfo_class(),
                "text": w.cget("text") if hasattr(w, "cget") else "",
                "bg": w.cget("bg") if hasattr(w, "cget") else "white",
                "fg": w.cget("fg") if hasattr(w, "cget") else "black",
                "font": str(w.cget("font")) if hasattr(w, "cget") else "",
                "x": w.winfo_x(),
                "y": w.winfo_y(),
                "width": w.winfo_width(),
                "height": w.winfo_height()
            }
            page.append(widget_info)
        layout.append(page)

    os.makedirs("assets", exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(layout, f, indent=2)

def export_code(frames):
    save_layout(frames)

    with open("generated_gui.py", "w") as f:
        f.write("import tkinter as tk\n\n")
        f.write("root = tk.Tk()\n")
        f.write("root.geometry('1000x600')\n\n")

        f.write("frames = []\n\n")

        with open(CONFIG_PATH, "r") as layout_file:
            layout = json.load(layout_file)

        for i, page in enumerate(layout):
            f.write(f"frame{i} = tk.Frame(root, bg='white')\n")
            f.write(f"frame{i}.pack(fill='both', expand=True)\n")
            f.write(f"frames.append(frame{i})\n\n")

            for w in page:
                font_line = f", font={repr(w['font'])}" if w['font'] else ""
                size_line = f", width={w['width']}, height={w['height']}"
                if w["type"] == "Button":
                    f.write(f"btn = tk.Button(frame{i}, text='{w['text']}', bg='{w['bg']}', fg='{w['fg']}'{font_line}{size_line})\n")
                    f.write(f"btn.place(x={w['x']}, y={w['y']})\n\n")
                elif w["type"] == "Label":
                    f.write(f"lbl = tk.Label(frame{i}, text='{w['text']}', bg='{w['bg']}', fg='{w['fg']}'{font_line}{size_line})\n")
                    f.write(f"lbl.place(x={w['x']}, y={w['y']})\n\n")
                elif w["type"] == "Entry":
                    f.write(f"ent = tk.Entry(frame{i}, bg='{w['bg']}'{font_line}{size_line})\n")
                    f.write(f"ent.place(x={w['x']}, y={w['y']})\n\n")

        f.write("root.mainloop()\n")

    if os.path.exists(CONFIG_PATH):
        os.remove(CONFIG_PATH)
