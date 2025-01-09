import tkinter as tk


class SettingsPage:
    def __init__(self, root):
        self.root = root

    def init_settings_page(self):
        settingsPage = tk.Frame(self.root, bg="#2C3E50")
        settingsPage.pack(fill="both", expand=True)

        titleLabel = tk.Label(
            settingsPage,
            text="Settings",
            fg="#ECF0F1",
            font=("Bahnschrift", 35, "bold"),
            bg="#2C3E50",
        )
        titleLabel.pack()
