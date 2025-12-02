import tkinter as tk
from tkinter import ttk, colorchooser
from gui_elements import (
    button, label, entry, textbox, checkbox, radiobutton, combobox,
    listbox, scale, spinbox, canvas, image, progressbar, notebook
)
from export.code_generator import export_code

class BuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter GUI Builder")
        self.root.geometry("1400x750")

        self.selected_widget = None
        self.frames = []
        self.current_frame_index = 0

        self.toolbar = ttk.Frame(root)
        self.toolbar.pack(side="top", fill="x")

        self.canvas_area = tk.Frame(root)
        self.canvas_area.pack(side="left", fill="both", expand=True)

        self.properties_panel = tk.Frame(root, bg="#f0f0f0", width=250)
        self.properties_panel.pack(side="right", fill="y")

        self.status_bar = ttk.Label(root, text="Ready", relief="sunken", anchor="w")
        self.status_bar.pack(side="bottom", fill="x")

        self.create_toolbar()
        self.create_new_frame()

    def update_status(self, message):
        self.status_bar.config(text=message)

    def create_toolbar(self):
        def add(name, func):
            ttk.Button(self.toolbar, text=name, command=lambda: self.add_widget(func)).pack(side="left")

        add("Button", button.create_button)
        add("Label", label.create_label)
        add("Entry", entry.create_entry)
        add("Text", textbox.create_textbox)
        add("Checkbox", checkbox.create_checkbox)
        add("Radiobutton", radiobutton.create_radiobutton)
        add("Combobox", combobox.create_combobox)
        add("Listbox", listbox.create_listbox)
        add("Scale", scale.create_scale)
        add("Spinbox", spinbox.create_spinbox)
        add("Canvas", canvas.create_canvas)
        add("Image", image.create_image)
        add("Progressbar", progressbar.create_progressbar)
        add("Notebook", notebook.create_notebook)

        ttk.Button(self.toolbar, text="New Page", command=self.create_new_frame).pack(side="left")
        ttk.Button(self.toolbar, text="Next Page", command=self.next_frame).pack(side="left")
        ttk.Button(self.toolbar, text="Export & Reset", command=self.export_and_reset).pack(side="right")

    def add_widget(self, func):
        widget = func(self.frames[self.current_frame_index], self.select_widget)
        self.update_status(f"{widget.winfo_class()} added")

    def create_new_frame(self):
        def apply_custom_size():
            width = int(width_var.get())
            height = int(height_var.get())
            frame = tk.Frame(self.canvas_area, bg="white", width=width, height=height)
            frame.pack(fill="both", expand=True)
            self.frames.append(frame)
            self.show_frame(len(self.frames) - 1)
            self.update_status(f"New page created ({width}x{height})")

        popup = tk.Toplevel(self.root)
        popup.title("Set Page Size")
        ttk.Label(popup, text="Width:").pack()
        width_var = tk.StringVar(value="1000")
        ttk.Entry(popup, textvariable=width_var).pack()

        ttk.Label(popup, text="Height:").pack()
        height_var = tk.StringVar(value="600")
        ttk.Entry(popup, textvariable=height_var).pack()

        ttk.Button(popup, text="Create Page", command=lambda: apply_custom_size() or popup.destroy()).pack(pady=10)


    def next_frame(self):
        if self.frames:
            self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)
            self.show_frame(self.current_frame_index)
            self.update_status(f"Switched to page {self.current_frame_index + 1}")

    def show_frame(self, index):
        for f in self.frames:
            f.pack_forget()
        self.frames[index].pack(fill="both", expand=True)

    def select_widget(self, widget):
        self.selected_widget = widget
        self.show_properties_panel(widget)
        self.update_status(f"{widget.winfo_class()} selected")
    def show_properties_panel(self, widget):
        for child in self.properties_panel.winfo_children():
            child.destroy()

        def label(text): ttk.Label(self.properties_panel, text=text).pack()
        def entry(var): ttk.Entry(self.properties_panel, textvariable=var).pack()

        # متن یا آیتم‌ها
        if isinstance(widget, (tk.Label, tk.Button, tk.Checkbutton, tk.Radiobutton)):
            label("Text:")
            text_var = tk.StringVar(value=widget.cget("text"))
            entry(text_var)
            ttk.Button(self.properties_panel, text="Apply Text", command=lambda: widget.config(text=text_var.get())).pack()

        elif isinstance(widget, tk.Text):
            label("Text:")
            text_var = tk.StringVar(value=widget.get("1.0", "end-1c"))
            entry(text_var)
            ttk.Button(self.properties_panel, text="Apply Text", command=lambda: widget.delete("1.0", "end") or widget.insert("1.0", text_var.get())).pack()

        elif isinstance(widget, tk.Listbox):
            label("Items (comma-separated):")
            items_var = tk.StringVar(value=", ".join(widget.get(0, tk.END)))
            entry(items_var)
            def apply_items():
                widget.delete(0, tk.END)
                for item in items_var.get().split(","):
                    widget.insert(tk.END, item.strip())
            ttk.Button(self.properties_panel, text="Apply Items", command=apply_items).pack()

        elif isinstance(widget, ttk.Combobox):
            label("Options (comma-separated):")
            options_var = tk.StringVar(value=", ".join(widget["values"]))
            entry(options_var)
            def apply_options():
                widget["values"] = [opt.strip() for opt in options_var.get().split(",")]
            ttk.Button(self.properties_panel, text="Apply Options", command=apply_options).pack()

        elif isinstance(widget, ttk.Progressbar):
            label("Progress Value:")
            val_var = tk.IntVar(value=widget["value"])
            entry(val_var)
            def apply_value():
                widget["value"] = val_var.get()
            ttk.Button(self.properties_panel, text="Apply Value", command=apply_value).pack()

            label("Mode:")
            mode_var = tk.StringVar(value=widget["mode"])
            entry(mode_var)
            def apply_mode():
                widget.config(mode=mode_var.get())
            ttk.Button(self.properties_panel, text="Apply Mode", command=apply_mode).pack()

        elif isinstance(widget, tk.Scale):
            label("From:")
            from_var = tk.IntVar(value=widget.cget("from"))
            entry(from_var)
            label("To:")
            to_var = tk.IntVar(value=widget.cget("to"))
            entry(to_var)
            def apply_range():
                widget.config(from_=from_var.get(), to=to_var.get())
            ttk.Button(self.properties_panel, text="Apply Range", command=apply_range).pack()

            label("Value:")
            val_var = tk.IntVar(value=widget.get())
            entry(val_var)
            def apply_value():
                widget.set(val_var.get())
            ttk.Button(self.properties_panel, text="Apply Value", command=apply_value).pack()

        elif isinstance(widget, tk.Spinbox):
            label("From:")
            from_var = tk.IntVar(value=int(widget.cget("from")))
            entry(from_var)
            label("To:")
            to_var = tk.IntVar(value=int(widget.cget("to")))
            entry(to_var)
            def apply_range():
                widget.config(from_=from_var.get(), to=to_var.get())
            ttk.Button(self.properties_panel, text="Apply Range", command=apply_range).pack()

            label("Value:")
            val_var = tk.StringVar(value=widget.get())
            entry(val_var)
            def apply_value():
                widget.delete(0, "end")
                widget.insert(0, val_var.get())
            ttk.Button(self.properties_panel, text="Apply Value", command=apply_value).pack()

        # رنگ‌ها
        label("Background:")
        bg_var = tk.StringVar(value=widget.cget("bg") if "bg" in widget.keys() else "white")
        entry(bg_var)
        ttk.Button(self.properties_panel, text="Apply BG", command=lambda: widget.config(bg=bg_var.get())).pack()
        ttk.Button(self.properties_panel, text="Pick BG Color", command=lambda: self.pick_color(bg_var, widget, "bg")).pack()

        if "fg" in widget.keys():
            label("Text Color:")
            fg_var = tk.StringVar(value=widget.cget("fg"))
            entry(fg_var)
            ttk.Button(self.properties_panel, text="Apply FG", command=lambda: widget.config(fg=fg_var.get())).pack()
            ttk.Button(self.properties_panel, text="Pick FG Color", command=lambda: self.pick_color(fg_var, widget, "fg")).pack()

        # فونت
        label("Font:")
        font_var = tk.StringVar(value="Segoe UI")
        entry(font_var)
        label("Font Size:")
        size_var = tk.IntVar(value=12)
        entry(size_var)
        if "font" in widget.keys():
            ttk.Button(self.properties_panel, text="Apply Font", command=lambda: widget.config(font=(font_var.get(), size_var.get()))).pack()

        # موقعیت
        label("X:")
        x_var = tk.IntVar(value=widget.winfo_x())
        entry(x_var)
        label("Y:")
        y_var = tk.IntVar(value=widget.winfo_y())
        entry(y_var)
        ttk.Button(self.properties_panel, text="Apply Position", command=lambda: widget.place(x=x_var.get(), y=y_var.get())).pack()

        # اندازه
        label("Width:")
        w_var = tk.IntVar(value=widget.winfo_width())
        entry(w_var)
        label("Height:")
        h_var = tk.IntVar(value=widget.winfo_height())
        entry(h_var)
        if "width" in widget.keys() and "height" in widget.keys():
            ttk.Button(self.properties_panel, text="Apply Size", command=lambda: widget.config(width=w_var.get(), height=h_var.get())).pack()

        ttk.Button(self.properties_panel, text="Delete Widget", command=lambda: widget.destroy()).pack(pady=10)

    def pick_color(self, var, widget, attr):
        color = colorchooser.askcolor()[1]
        if color:
            var.set(color)
            widget.config(**{attr: color})
            self.update_status(f"{attr} color updated")

    def export_and_reset(self):
        export_code(self.frames)
        self.update_status("Layout exported")

if __name__ == "__main__":
    root = tk.Tk()
    app = BuilderApp(root)
    root.mainloop()
