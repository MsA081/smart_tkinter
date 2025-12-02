def make_draggable(widget, select_callback=None):
    def on_drag_start(event):
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y
        if select_callback:
            select_callback(widget)

    def on_drag_motion(event):
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y() - widget._drag_start_y + event.y
        widget.place(x=x, y=y)

    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)
