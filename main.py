import tkinter as tk
import sys

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
WINDOW_X_OFFSET = 0
WINDOW_Y_OFFSET = 0

TIME_ALERTS = [
    {"minute": 0, "second": 10, "message": "Gavel One Time"},
    {"minute": 0, "second": 15, "message": "Gavel Two Times"},
    {"minute": 2, "second": 55, "message": "Gavel Three Times"},
    {"minute": 3, "second": 0, "message": "Stand Up and Gavel Down"},
]

WARNING_TIME = 10


class OverlayApp:
    def __init__(self):
        self.root = tk.Tk()
        self.timer = 0
        self.timerStatus = False
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

        startEndButtons = tk.Frame(startPage, bg="#2C3E50")
        startEndButtons.pack()

        startButton = tk.Button(
            startEndButtons,
            text="Start Timer",
            command=lambda: (
                self.clear_all_widgets(),
                self.init_timer_page(),
            ),
            font=("Bahnschrift", 15, "normal"),
        )
        startButton.pack()

        exitButton = tk.Button(
            startEndButtons,
            text="Exit",
            command=lambda: sys.exit(),
            font=("Bahnschrift", 10, "normal"),
        )
        exitButton.pack()

        # startEndButtons.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def init_timer_page(self):
        timerPage = tk.Frame(self.root, bg="#2C3E50")
        timerPage.pack(fill="both", expand=True)

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
            font=("Bahnschrift", 20, "normal"),
            bg="#2C3E50",
            wraplength=WINDOW_WIDTH - 60,
        )
        alertLabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        stopButton = tk.Button(
            timerPage,
            text="Stop Timer",
            command=lambda: setattr(self, "timerStatus", True),
        )
        stopButton.pack()

        self.root.after(1000, self.run_timer, timeLabel, alertLabel, stopButton)

    def run_timer(self, timeLabel, alertLabel, stopButton):

        alertLabel.config(text="")

        self.timer = self.timer + 1
        minutes = self.timer // 60
        seconds = self.timer % 60
        formattedTime = f"{minutes}:{seconds <= 9 and '0'+str(seconds) or seconds}"

        timeLabel.config(text=formattedTime)

        for alert in TIME_ALERTS:
            if (minutes == alert["minute"]) and (
                (seconds <= alert["second"])
                and (seconds >= alert["second"] - WARNING_TIME)
            ):
                multipleNewLine = ""
                if alertLabel.cget("text") != "":
                    multipleNewLine = alertLabel.cget("text") + "\n"
                secondsToAlert = alert["second"] - seconds
                alertLabel.config(
                    text=f'{multipleNewLine}{alert["message"]} in {alert["minute"] - minutes}:{secondsToAlert <= 9 and "0"+str(secondsToAlert) or secondsToAlert}'
                )
                break
            else:
                alertLabel.config(text="")
                break

        if self.timerStatus == False:
            self.root.after(1000, self.run_timer, timeLabel, alertLabel, stopButton)
        else:
            self.timerStatus = False
            self.clear_all_widgets()
            self.init_home_page()

    def clear_all_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

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
