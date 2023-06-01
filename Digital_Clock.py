#!/usr/bin/env python
# ^ this should work fine in a virtual environment

import tkinter as tk
import datetime
import time

from Timer import Timer
from Clock import Clock
from Stopwatch import Stopwatch
    
class DigitalClockFrame():
    def __init__(self, parent) -> None:
        self.parent = parent

        self.parent.title("Digital Clock App")
        self.parent.geometry('500x150') #x,y
        self.parent.resizable(False, False) #x,y
        # TODO: add an icon -> keyword: iconphoto
        
        # Digital clock face is contained here
        self.clock_face = tk.Frame(master=self.parent)
        self.clock_face.pack(fill=tk.BOTH, expand=True)
        self.clock_face.pack_propagate(False)
        
        # top row
        # TODO: add a clock here when the clock is not displayed underneath.
        # Could be next to the date
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
        
        self.clock_btn = tk.Button(master=self.button_area, text="Clock")
        self.clock_btn.pack(side=tk.LEFT)

        self.timer_btn = tk.Button(master=self.button_area, text="Timer")
        self.timer_btn.pack(side=tk.LEFT)

        self.stop_watch_btn = tk.Button(master=self.button_area, text="Stop Watch")
        self.stop_watch_btn.pack(side=tk.LEFT)
        
    def bottom_btn_row():
        return 1
    

if __name__ == "__main__":
    app = tk.Tk()
    DigitalClockFrame(app)
    app.mainloop()


# TODO: add these sounds and fonts

# alarm sound from pixabay.com link to source:
# https://pixabay.com/sound-effects/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=72117

# fonts from 1001fonts.com link to source:
# https://www.1001fonts.com/digital-fonts.html