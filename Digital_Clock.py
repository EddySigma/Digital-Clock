#!/usr/bin/env python
# ^ this should work fine in a virtual environment

import tkinter as tk
import datetime
import time
    
class DigitalClockFrame():
    def __init__(self, parent) -> None:
        self.parent = parent

        self.parent.title("Digital Clock App")
        self.parent.geometry('250x150') #x,y
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
        Clock(self.mid_row)

        # will be used to house a cycling button
        self.right_column = tk.Frame(master=self.mid_row, width=20)
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
        self.am_pm_font_size = 20
        self.isAm = True

        # holds the actual clock display (numbers + am/pm)
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


if __name__ == "__main__":
    app = tk.Tk()
    DigitalClockFrame(app)
    app.mainloop()


# alarm sound from pixabay.com link to source:
# https://pixabay.com/sound-effects/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=72117

# fonts from 1001fonts.com link to source:
# https://www.1001fonts.com/digital-fonts.html