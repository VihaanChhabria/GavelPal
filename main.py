import tkinter as tk
import sys

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
WINDOW_X_OFFSET = 0
WINDOW_Y_OFFSET = 0

class OverlayApp:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.init_overlay()

    def setup_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_x = screen_width - WINDOW_WIDTH + WINDOW_X_OFFSET
        window_y = screen_height - WINDOW_HEIGHT + WINDOW_Y_OFFSET
        
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{window_x}+{window_y}")
        self.root.overrideredirect(True)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.wm_attributes("-topmost", 1)

    def init_overlay(self):
        self.root.config(bg="gray")

    def on_closing(self):
        sys.exit()

    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            sys.exit()

if __name__ == "__main__":
    app = OverlayApp()
    app.run()

