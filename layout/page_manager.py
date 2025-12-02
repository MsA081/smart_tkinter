import tkinter as tk

class PageManager:
    def __init__(self, canvas_area):
        self.canvas_area = canvas_area
        self.frames = []
        self.current_index = 0

    def create_new_page(self):
        frame = tk.Frame(self.canvas_area, bg="white", width=1000, height=600)
        frame.pack(fill="both", expand=True)
        self.frames.append(frame)
        self.show_page(len(self.frames) - 1)

    def next_page(self):
        if self.frames:
            self.current_index = (self.current_index + 1) % len(self.frames)
            self.show_page(self.current_index)

    def show_page(self, index):
        for f in self.frames:
            f.pack_forget()
        self.frames[index].pack(fill="both", expand=True)

    def get_current_frame(self):
        if self.frames:
            return self.frames[self.current_index]
        return None
