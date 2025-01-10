import tkinter as tk
import sys

from utils import clear_all_widgets


class HomePage:
    def __init__(self, root):
        self.root = root

        self.init_timer_page = None
        self.init_settings_page = None

    def init_home_page(self):
        self.root.config(bg="#2C3E50")

        startPage = tk.Frame(self.root, bg="#2C3E50")
        startPage.pack()

        title = tk.Label(
            startPage,
            text="Gavel Pal",
            fg="#ECF0F1",
            font=("Bahnschrift", 45, "bold"),
            bg="#2C3E50",
        )
        title.pack()

        startEndButtons = tk.Frame(startPage, bg="#2C3E50")
        startEndButtons.pack()

        startButton = tk.Button(
            startEndButtons,
            text="Start Timer",
            command=lambda: (
                clear_all_widgets(self),
                self.init_timer_page(),
            ),
            font=("Bahnschrift", 15, "normal"),
        )
        startButton.pack()

        settingsButton = tk.Button(
            startEndButtons,
            text="Settings",
            command=lambda: (
                # clear_all_widgets(self),
                # self.init_settings_page(),
            ),
            font=("Bahnschrift", 10, "normal"),
        )
        settingsButton.pack()

        exitButton = tk.Button(
            startEndButtons,
            text="Exit",
            command=lambda: sys.exit(),
            font=("Bahnschrift", 10, "normal"),
        )
        exitButton.pack()

        creditsLabel = tk.Label(
            startPage,
            text="Made by Vihaan Chhabria",
            fg="#ECF0F1",
            font=("Bahnschrift", 10, "normal"),
            bg="#2C3E50",
        )
        creditsLabel.pack()
