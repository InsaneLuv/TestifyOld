from PySide6.QtCore import QTimer, QTime

class TimerManager:
    def __init__(self, total_time_minutes, update_callback):
        self.total_time_seconds = total_time_minutes * 60
        self.elapsed_time_seconds = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.update_callback = update_callback

    def start_timer(self):
        self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()

    def update_timer(self):
        self.elapsed_time_seconds += 1
        remaining_time = self.calculate_remaining_time()
        self.update_callback(remaining_time)

        if remaining_time == QTime(0, 0):
            self.timer.stop()

    def calculate_remaining_time(self):
        remaining_time_seconds = max(0, self.total_time_seconds - self.elapsed_time_seconds)
        remaining_time = QTime(0, 0).addSecs(remaining_time_seconds)
        return remaining_time