def apply_position(widget, x, y):
    widget.place(x=x, y=y)

def apply_size(widget, width, height):
    widget.config(width=width, height=height)

def apply_font(widget, font_name, font_size):
    widget.config(font=(font_name, font_size))

def apply_colors(widget, bg=None, fg=None):
    if bg:
        widget.config(bg=bg)
    if fg:
        widget.config(fg=fg)

def apply_text(widget, text):
    widget.config(text=text)
