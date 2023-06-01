import tkinter as tk
import datetime

# TODO: modify this to import it into Digital_Clock.py


class Clock(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.overall_font = 0
        self.clock_font = "Arial" # placeholder
        self.time_font_size = 35

        # holds the actual clock display
        self.clock_frame = tk.Frame(master=container)
        self.clock_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.clock_frame.pack_propagate(False)

        # clock time
        self.clock_time = tk.Label(
            master=self.clock_frame,
            font=(self.clock_font, self.time_font_size))
        self.clock_time.pack(side=tk.LEFT)
        self.time_now()
    
    def time_now(self):
        current_time = datetime.datetime.now().time().strftime("%H:%M:%S %p")
        self.clock_time.config(text=current_time)
        self.clock_time.after(200, self.time_now)