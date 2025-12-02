import json
import os
import tkinter as tk
from tkinter import ttk

CONFIG_PATH = "assets/config.json"

def make_json_serializable(obj):
    """تبدیل اشیاء غیر JSON serializable به string"""
    if hasattr(obj, '__str__'):
        return str(obj)
    elif isinstance(obj, (list, tuple)):
        return [make_json_serializable(item) for item in obj]
    elif isinstance(obj, dict):
        return {make_json_serializable(k): make_json_serializable(v) for k, v in obj.items()}
    return str(obj)

def save_layout(frames):
    layout = []
    for i, frame in enumerate(frames):
        page = []
        for w in frame.winfo_children():
            widget_info = {
                "type": w.winfo_class(),
                "text": w.cget("text") if "text" in w.keys() else "",
                "bg": w.cget("bg") if "bg" in w.keys() else "white",
                "fg": w.cget("fg") if "fg" in w.keys() else "black",
                "font": make_json_serializable(w.cget("font")) if "font" in w.keys() else "",
                "x": w.winfo_x(),
                "y": w.winfo_y(),
                "width": w.winfo_width(),
                "height": w.winfo_height(),
                "from_": w.cget("from") if "from" in w.keys() else "",
                "to": w.cget("to") if "to" in w.keys() else "",
                "orient": w.cget("orient") if "orient" in w.keys() else "",
                "value": str(w.cget("value")) if "value" in w.keys() else "",
                "values": make_json_serializable(w.cget("values")) if "values" in w.keys() else ""
            }
            page.append(widget_info)
        layout.append(page)

    os.makedirs("assets", exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(layout, f, indent=2, default=str)

def export_code(frames):
    save_layout(frames)

    with open("generated_gui.py", "w") as f:
        f.write("import tkinter as tk\n")
        f.write("from tkinter import ttk\n")
        f.write("from PIL import Image, ImageTk\n")
        f.write("import os\n\n")
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
                font_line = f", font={repr(w['font'])}" if w['font'] and w['font'] != 'None' else ""
                size_line = f", width={int(w['width'])}, height={int(w['height'])}" if w['width'] and w['height'] else ""
                from_line = f", from_={w['from_']}" if w['from_'] else ""
                to_line = f", to={w['to']}" if w['to'] else ""
                orient_line = f", orient='{w['orient']}'" if w['orient'] else ""
                value_line = f".set({w['value']})" if w['value'] else ""
                values_line = f", values={repr(w['values'])}" if w['values'] else ""
                
                if w["type"] == "Button":
                    f.write(f"btn = tk.Button(frame{i}, text='{w['text']}', bg='{w['bg']}', fg='{w['fg']}'{font_line}{size_line})\n")
                    f.write(f"btn.place(x={int(w['x'])}, y={int(w['y'])})\n\n")
                    
                elif w["type"] == "Label":
                    f.write(f"lbl = tk.Label(frame{i}, text='{w['text']}', bg='{w['bg']}', fg='{w['fg']}'{font_line}{size_line})\n")
                    f.write(f"lbl.place(x={int(w['x'])}, y={int(w['y'])})\n\n")
                    
                elif w["type"] == "Entry":
                    f.write(f"ent = tk.Entry(frame{i}, bg='{w['bg']}'{font_line}{size_line})\n")
                    f.write(f"ent.place(x={int(w['x'])}, y={int(w['y'])})\n\n")
                    
                elif w["type"] == "Text":
                    f.write(f"txt = tk.Text(frame{i}, width=30, height=5, bg='{w['bg']}', fg='{w['fg']}'{font_line})\n")
                    f.write(f"txt.place(x={int(w['x'])}, y={int(w['y'])})\n\n")
                    
                elif w["type"] == "Spinbox":
                    f.write(f"spn = tk.Spinbox(frame{i}{from_line}{to_line}{size_line})\n")
                    f.write(f"spn.place(x={int(w['x'])}, y={int(w['y'])})\n\n")
                    
                elif w["type"] == "Scale":
                    f.write(f"scl = tk.Scale(frame{i}{from_line}{to_line}{orient_line}{size_line})\n")
                    f.write(f"scl.place(x={int(w['x'])}, y={int(w['y'])})\n")
                    if value_line:
                        f.write(f"scl{value_line}\n\n")
                    else:
                        f.write("\n")
                    
                elif w["type"] == "Radiobutton":
                    f.write(f"var_r{i} = tk.IntVar()\n")
                    f.write(f"rbtn = tk.Radiobutton(frame{i}, text='{w['text']}', variable=var_r{i}, value=1, bg='{w['bg']}', fg='{w['fg']}'{font_line})\n")
                    f.write(f"rbtn.place(x={int(w['x'])}, y={int(w['y'])})\n\n")
                    
                elif w["type"] == "Checkbutton":
                    f.write(f"var_c{i} = tk.BooleanVar()\n")
                    f.write(f"chk = tk.Checkbutton(frame{i}, text='{w['text']}', variable=var_c{i}, bg='{w['bg']}', fg='{w['fg']}'{font_line})\n")
                    f.write(f"chk.place(x={int(w['x'])}, y={int(w['y'])})\n\n")
                    
                elif w["type"] == "Listbox":
                    f.write(f"lst = tk.Listbox(frame{i}, bg='{w['bg']}', fg='{w['fg']}', font=('Segoe UI', 10){size_line})\n")
                    f.write(f"lst.insert(0, 'Item 1')\n")
                    f.write(f"lst.insert(1, 'Item 2')\n")
                    f.write(f"lst.insert(2, 'Item 3')\n")
                    f.write(f"lst.place(x={int(w['x'])}, y={int(w['y'])})\n\n")
                    
                elif w["type"] == "Canvas":
                    f.write(f"cvs = tk.Canvas(frame{i}, width=200, height=150, bg='lightyellow', highlightthickness=1, highlightbackground='gray')\n")
                    f.write(f"cvs.create_rectangle(20, 20, 100, 100, fill='blue')\n")
                    f.write(f"cvs.place(x={int(w['x'])}, y={int(w['y'])})\n\n")
                    
                elif w["type"] == "TCombobox":
                    f.write(f"combo = ttk.Combobox(frame{i}{values_line})\n")
                    f.write(f"combo.place(x={int(w['x'])}, y={int(w['y'])}, width=150)\n\n")
                    
                elif w["type"] == "TNotebook":
                    f.write(f"nb = ttk.Notebook(frame{i})\n")
                    f.write(f"frame_nb1 = tk.Frame(nb, bg='white')\n")
                    f.write(f"frame_nb2 = tk.Frame(nb, bg='white')\n")
                    f.write(f"nb.add(frame_nb1, text='Tab 1')\n")
                    f.write(f"nb.add(frame_nb2, text='Tab 2')\n")
                    f.write(f"nb.place(x={int(w['x'])}, y={int(w['y'])}, width=200, height=100)\n\n")
                    
                elif w["type"] == "TProgressbar":
                    f.write(f"pbar = ttk.Progressbar(frame{i}, orient='horizontal', length=150, mode='determinate')\n")
                    f.write(f"pbar.place(x={int(w['x'])}, y={int(w['y'])})\n")
                    f.write(f"pbar['value'] = 50\n\n")

        f.write("root.mainloop()\n")

    if os.path.exists(CONFIG_PATH):
        os.remove(CONFIG_PATH)
