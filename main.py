import tkinter as tk
import sys

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
WINDOW_X_OFFSET = 0
WINDOW_Y_OFFSET = 0

TIME_ALERTS = [
    {"time": "2:00", "alert": "Gavel One Time"},
    {"time": "2:30", "alert": "Gavel Two Times"},
    {"time": "2:55", "alert": "Gavel Three Times"},
    {"time": "3:00", "alert": "Stand Up and Gavel Down"},
]


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

        startButton = tk.Button(
            startPage,
            text="Start Timer",
            command=lambda: (
                self.clear_all_widgets(),
                self.init_timer_page(),
            ),
        )
        startButton.pack()

        exitButton = tk.Button(startPage, text="Exit", command=lambda: sys.exit())
        exitButton.pack()

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
            text="e",
            fg="#ECF0F1",
            font=("Bahnschrift", 35, "normal"),
            bg="#2C3E50",
            wraplength=WINDOW_WIDTH - 50,
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
        self.timer = self.timer + 1
        minutes = self.timer // 60
        seconds = self.timer % 60
        formattedTime = f"{minutes}:{seconds <= 9 and '0'+str(seconds) or seconds}"
        # print(formattedTime)
        # print(f"{minutes}:{seconds + 5}\n")
        # print(self.timerStatus)

        timeLabel.config(text=formattedTime)

        forwardedTimer = self.timer + 5
        forwardedMinutes = forwardedTimer // 60
        forwardedSeconds = forwardedTimer % 60
        forwardedFormattedTime = f"{forwardedMinutes}:{forwardedSeconds <= 9 and '0'+str(forwardedSeconds) or forwardedSeconds}"

        for alert in TIME_ALERTS:
            if forwardedFormattedTime == alert["time"]:
                print("HERE______HERE______")
                alertLabel.config(text=alert["alert"])
                break
            elif formattedTime == alert["time"]:
                print("FINISHED______FINISHED______")
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
