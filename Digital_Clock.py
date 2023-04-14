#!/usr/bin/env python
# ^ this should work fine in a virtual environment

import tkinter as tk
import datetime
import time
    
class DigitalClockFrame():
    def __init__(self, parent) -> None:
        self.parent = parent

        self.parent.title("Digital Clock App")
        self.parent.geometry('325x150') #x,y
        self.parent.resizable(False, False) #x,y
        
        # Digital clock face is contained here
        self.clock_face = tk.Frame(master=self.parent)
        self.clock_face.pack(fill=tk.BOTH, expand=True)
        self.clock_face.pack_propagate(False)
        
        # top row
        self.top_row = tk.Frame(master=self.clock_face, height=20, bg="red")
        self.top_row.pack(fill=tk.X, side=tk.TOP)
        
        # Today's date
        self.title_label = tk.Label(
            master=self.top_row,
            text=datetime.datetime.today().strftime("%B %d, %Y"),
            bg="red")
        self.title_label.pack(side=tk.TOP)
        
        # middle row
        self.mid_row = tk.Frame(master=self.clock_face)
        self.mid_row.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.mid_row.pack_propagate(False)

        # will be used to house a cycling button
        self.left_column = tk.Frame(master=self.mid_row, width=20)
        self.left_column.pack(fill=tk.Y, side=tk.LEFT)
        self.left_column.pack_propagate(False)

        self.left_btn = tk.Button(master=self.left_column, text="<")
        self.left_btn.pack(side=tk.LEFT, fill=tk.BOTH)

        # TODO: insert the utility frame here ==========================
        #Clock(self.mid_row)
        #Stopwatch(self.mid_row)
        Timer(self.mid_row)

        # will be used to house a cycling button
        self.right_column = tk.Frame(master=self.mid_row, width=20, bg="blue")
        self.right_column.pack(fill=tk.Y, side=tk.RIGHT)
        self.right_column.pack_propagate(False)
        
        self.right_btn = tk.Button(master=self.right_column, text=">")
        self.right_btn.pack(side=tk.RIGHT, fill=tk.BOTH)

        # bottom row
        self.bottom_row = tk.Frame(master=self.clock_face, height=20)
        self.bottom_row.pack(fill=tk.X, side=tk.BOTTOM)
        self.bottom_row.pack_propagate(False)

        # TODO: replace with function that takes a list of items
        # button section
        self.button_area = tk.Frame(master=self.bottom_row)
        self.button_area.pack(side=tk.BOTTOM)
        """
        self.clock_btn = tk.Button(master=self.button_area, text="Clock")
        self.clock_btn.pack(side=tk.LEFT)

        self.timer_btn = tk.Button(master=self.button_area, text="Timer")
        self.timer_btn.pack(side=tk.LEFT)

        self.stop_watch_btn = tk.Button(master=self.button_area, text="Stop Watch")
        self.stop_watch_btn.pack(side=tk.LEFT)
        """
    def bottom_btn_row(): # takes list of buttons
        return 1
    
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

class Timer(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # holder for everything
        self.timer_frame = tk.Frame(master=container)
        self.timer_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.timer_frame.pack_propagate(False)

        # top row of buttons to increase time in h/m/s
        self.inc_hour = tk.Button(master=self.timer_frame, text='^').grid(column=0, row=0) # inc -> increase
        self.inc_minute = tk.Button(master=self.timer_frame).grid(column=2, row=0)
        self.inc_second = tk.Button(master=self.timer_frame).grid(column=4, row=0)

        # label row to inform user of hh:mm:ss
        self.hour_lbl = tk.Label(master=self.timer_frame, text="Hour").grid(column=0, row=1)
        self.minute_lbl = tk.Label(master=self.timer_frame, text="Minute").grid(column=2, row=1)
        self.second_lbl = tk.Label(master=self.timer_frame, text="Second").grid(column=4, row=1)

        # time labels for hh:mm:ss
        self.timer_hour_lbl = tk.Label(master=self.timer_frame, text="00").grid(column=0, row=2)
        self.h_m_div_lbl = tk.Label(master=self.timer_frame, text=":").grid(column=1, row=2)
        self.timer_minute_lbl = tk.Label(master=self.timer_frame, text="00").grid(column=2, row=2)
        self.m_s_div_lbl = tk.Label(master=self.timer_frame, text=":").grid(column=3, row=2)
        self.timer_second_lbl = tk.Label(master=self.timer_frame, text="00").grid(column=4, row=2)

        # bottom button row for hh:mm:ss
        self.dec_hour = tk.Button(master=self.timer_frame).grid(column=0, row=3) # dec -> decrease
        self.dec_minute = tk.Button(master=self.timer_frame).grid(column=2, row=3)
        self.dec_second = tk.Button(master=self.timer_frame).grid(column=4, row=3)
        
        # start button
        self.start_btn = tk.Button(master=container)

if __name__ == "__main__":
    app = tk.Tk()
    DigitalClockFrame(app)
    app.mainloop()


# alarm sound from pixabay.com link to source:
# https://pixabay.com/sound-effects/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=72117

# fonts from 1001fonts.com link to source:
# https://www.1001fonts.com/digital-fonts.html