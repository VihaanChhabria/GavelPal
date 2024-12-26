import tkinter as tk

from utils import clear_all_widgets

TIME_ALERTS = [
    {"minute": 2, "second": 0, "message": "Gavel One Time"},
    {"minute": 2, "second": 30, "message": "Gavel Two Times"},
    {"minute": 2, "second": 55, "message": "Gavel Three Times"},
    {"minute": 3, "second": 0, "message": "Stand Up and Gavel Down"},
    {"minute": 3, "second": 10, "message": "Verbal Cutoff"},
]
WARNING_TIME = 15
END_TIME = {"minute": 3, "second": 10}


class TimerPage:
    def __init__(self, root, WINDOW_GEOMETRY):
        self.root = root
        self.init_home_page = None
        self.WINDOW_GEOMETRY = WINDOW_GEOMETRY

        self.timer = 0
        self.timerStatus = False

    def init_timer_page(self):
        self.timer = 0

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
            fg="#E65F5C",
            font=("Bahnschrift", 20, "bold"),
            bg="#2C3E50",
            wraplength=self.WINDOW_GEOMETRY["width"] - 60,
        )
        alertLabel.place(x=150, y=200, anchor=tk.CENTER)

        stopButton = tk.Button(
            timerPage,
            text="Stop Timer",
            command=lambda: setattr(self, "timerStatus", True),
        )
        stopButton.pack()

        self.root.after(1000, self.run_timer, timeLabel, alertLabel, stopButton)

    def run_timer(self, timeLabel, alertLabel, stopButton):
        def format_time(minutes, seconds):
            return f"{minutes}:{seconds <= 9 and '0'+str(seconds) or seconds}"

        alertLabel.config(text="")

        self.timer = self.timer + 1
        minutes = self.timer // 60
        seconds = self.timer % 60
        currentFormattedTime = format_time(minutes, seconds)

        timeLabel.config(text=currentFormattedTime)

        for alert in TIME_ALERTS:
            alertPlainTime = (alert["minute"] * 60) + alert["second"]
            if (self.timer <= alertPlainTime) and (
                self.timer >= alertPlainTime - WARNING_TIME
            ):
                secondsToAlert = alertPlainTime - self.timer
                alertLabel.config(
                    text=f'{alertLabel.cget("text")}{alert["message"]} in {format_time(0, secondsToAlert)}\n'
                )
            else:
                nonExpiredMessage = alertLabel.cget("text").replace(
                    f'{alert["message"]} in 0:00\n', ""
                )
                alertLabel.config(text=nonExpiredMessage)

        if (self.timerStatus == False) and (
            self.timer < (END_TIME["minute"] * 60 + END_TIME["second"])
        ):
            self.root.after(1000, self.run_timer, timeLabel, alertLabel, stopButton)
        else:
            self.timerStatus = False
            clear_all_widgets(self)
            self.init_home_page()
