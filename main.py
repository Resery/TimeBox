import rumps
import time
import sqlite3
import os

class TimerApp(object):
    def __init__(self) -> None:
        self.app = rumps.App("TimeBox","Resery's Pomodoro 🛎")

        self.start_pause_button = rumps.MenuItem(
            title = "Start Timer",
            callback = None,
            key = "p",
        )

        self.stop_button = rumps.MenuItem(
            title = "",
            callback = None,
            key = "s",
        )

        self.sync_button = rumps.MenuItem(
            title = "Sync",
            callback = None,
            key = "r",
        )


        self.app.menu = [
            self.start_pause_button,
            None,
            self.sync_button,
            None
        ]

    def run(self):
        self.app.run()

if __name__ == "__main__":
    app = TimerApp()
    app.run()