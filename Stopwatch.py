import tkinter as tk
import datetime

# TODO modify this file to import it into Digital_Clock.py

class Stopwatch(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # TODO: move settings out of here
        self.clock_font = "Arial" # placeholder

        # stopwatch state
        self.is_running = False
        self.is_start_active = True
        self.is_stop_active = False
        self.is_clear_active = False

        self.time_font_size = 35
        self.time_counter = 28800 #66600 # Why does time not start at 0? for me it starts at 16 hrs
        self.day_in_seconds = 86400 # 60*60*24

        # area to display
        self.stopwatch_frame = tk.Frame(master=container)
        self.stopwatch_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.stopwatch_frame.pack_propagate(False)

        # elapsed time display
        self.stopwatch_lbl = tk.Label(
            master=self.stopwatch_frame,
            font=(self.clock_font, self.time_font_size))
        self.stopwatch_lbl.pack(side=tk.LEFT)
        self.display_counter()

        self.control_btns_frame = tk.Frame(master=self.stopwatch_frame)
        self.control_btns_frame.pack(side=tk.RIGHT)

        # start button
        self.start_btn = tk.Button(
            master=self.control_btns_frame,
            text="Start",
            bg="green",
            command=self.start_click)
        self.start_btn.pack(fill=tk.X, side=tk.TOP)

        # stop button
        self.stop_btn = tk.Button(
            master=self.control_btns_frame,
            text="Stop",
            bg="red",
            state='disabled',
            command=self.stop_click)
        self.stop_btn.pack(fill=tk.X, side=tk.TOP)

        # clear button
        self.clear_btn = tk.Button(
            master=self.control_btns_frame,
            text="Clear",
            state='disabled',
            command=self.clear_click)
        self.clear_btn.pack(fill=tk.X, side=tk.BOTTOM)

    def display_counter(self):
        elapsed_time = datetime.datetime.fromtimestamp(self.time_counter)
        elapsed_time_str = elapsed_time.strftime("%H:%M:%S")
        self.stopwatch_lbl.config(text=elapsed_time_str)

        if self.is_running:
            """ Something to look into. Due to the time set to 1000 milisecs when stop gets
            clicked the timer will wait until the second finishes. Is there a way to make this
            a little more seemless? I tried looking into displaying 10ths or 100ths of a second
            but I could not find much only microseconds and that is very much overkill for this.
            """
            self.stopwatch_lbl.after(1000, self.display_counter)
            self.time_counter += 1

    def start_click(self):
        self.is_running = True
        self.display_counter()
        self.start_btn['state'] = 'disabled'
        self.stop_btn['state'] = 'normal'
        self.clear_btn['state'] = 'normal'

    def stop_click(self):
        self.is_running = False
        self.start_btn['state'] = 'normal'
        self.stop_btn['state'] = 'disabled'

    def clear_click(self):
        self.is_running = False
        self.time_counter = 28800
        self.display_counter()
        self.start_btn['state'] = 'normal'
        self.stop_btn['state'] = 'disabled'
        self.clear_btn['state'] = 'disabled'