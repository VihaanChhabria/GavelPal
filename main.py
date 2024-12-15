import tkinter as tk
import sys

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
WINDOW_X_OFFSET = 0
WINDOW_Y_OFFSET = 0


class OverlayApp:
    def __init__(self):
        self.root = tk.Tk()
        self.timer = 0
        self.setup_window()
        self.init_home_page()

    def setup_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_x = screen_width - WINDOW_WIDTH + WINDOW_X_OFFSET
        window_y = screen_height - WINDOW_HEIGHT + WINDOW_Y_OFFSET

        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{window_x}+{window_y}")
        self.root.overrideredirect(True)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.wm_attributes("-topmost", 1)

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

        startButton = tk.Button(
            startPage,
            text="Start Timer",
            command=lambda: (
                startPage.pack_forget(),
                self.init_timer_page(),
            ),
        )
        startButton.pack()

    def init_timer_page(self):
        timerPage = tk.Frame(self.root, bg="#2C3E50")
        timerPage.pack()

        timeLabel = tk.Label(
            timerPage,
            text="0:00",
            fg="#ECF0F1",
            font=("Bahnschrift", 45, "normal"),
            bg="#2C3E50",
        )
        timeLabel.pack()

        alertLabel = tk.Label(
            timerPage,
            text="",
            fg="#ECF0F1",
            font=("Bahnschrift", 35, "normal"),
            bg="#2C3E50",
        )
        alertLabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.root.after(1000, self.run_timer, timeLabel)

    def run_timer(self, timeLabel):
        self.timer = self.timer + 1
        minutes = self.timer // 60
        seconds = self.timer % 60
        formattedTime = f"{minutes}:{seconds <= 9 and '0'+str(seconds) or seconds}"
        print(formattedTime)

        timeLabel.config(text=formattedTime)
        self.root.after(1000, self.run_timer, timeLabel)

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
