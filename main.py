import tkinter as tk
import sys

from pages.home_page import HomePage
from pages.timer_page import TimerPage
from pages.settings_page import SettingsPage

WINDOW_GEOMETRY = {
    "width": 300,
    "height": 300,
    "x_offset": 0,
    "y_offset": 0,
}


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()

        self.home_page = HomePage(self.root)
        self.timer_page = TimerPage(self.root, WINDOW_GEOMETRY)
        self.settings_page = SettingsPage(self.root)

        self.home_page.init_timer_page = self.timer_page.init_timer_page
        self.home_page.init_settings_page = self.settings_page.init_settings_page
        self.timer_page.init_home_page = self.home_page.init_home_page

        self.home_page.init_home_page()

    def setup_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_x = screen_width - WINDOW_GEOMETRY["width"] + WINDOW_GEOMETRY["x_offset"]
        window_y = (
            screen_height - WINDOW_GEOMETRY["height"] + WINDOW_GEOMETRY["y_offset"]
        )

        self.root.geometry(
            f"{WINDOW_GEOMETRY['width']}x{WINDOW_GEOMETRY['height']}+{window_x}+{window_y}"
        )
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", 1)

    def run(self):
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":
    app = App()
    app.run()
