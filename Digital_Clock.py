#!/usr/bin/env python
# ^ this should work fine in a virtual environment

import tkinter as tk

class Digi_Clock(tk.Tk):
    # initial settings
    border_width = 20
    overall_font = 0
    clock_font = "Arial" # placeholder
    time_font_size = 35
    am_pm_font_size = 20
    current_time = "12:34"
    isAm = True
    today = "April 3, 2023" # placeholder

    def __init__(self):
        super().__init__()

        # root window configuration
        self.title("Digital Clock")
        self.geometry('250x150')

        # Digital clock face is contained here
        self.clock_face = tk.Frame(master=self, width=200, height=150)
        self.clock_face.pack(fill=tk.BOTH, expand=True)
        self.clock_face.pack_propagate(False)

        # top row
        self.top_row = tk.Frame(master=self.clock_face, height=self.border_width, bg="red")
        self.top_row.pack(fill=tk.X, side=tk.TOP)

        # date/other
        self.title_label = tk.Label(master=self.top_row, text=self.today)
        self.title_label.pack(side=tk.TOP)

        # middle row
        self.mid_row = tk.Frame(master=self.clock_face)
        self.mid_row.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.mid_row.pack_propagate(False)

        # will be used to house a cycling button
        self.left_column = tk.Frame(master=self.mid_row, width=self.border_width, bg='blue')
        self.left_column.pack(fill=tk.Y, side=tk.LEFT)
        self.left_column.pack_propagate(False)

        self.left_btn = tk.Button(master=self.left_column, text="<")
        self.left_btn.pack(side=tk.LEFT)

        # holds the actual clock display (numbers + am/pm)
        self.clock_frame = tk.Frame(master=self.mid_row, bg="yellow")
        self.clock_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.clock_frame.pack_propagate(False)

        # clock time
        self.clock_time = tk.Label(master=self.clock_frame, text=self.current_time, font=(self.clock_font, self.time_font_size))
        self.clock_time.pack(side=tk.LEFT)

        # time state
        self.time_state = tk.Frame(master=self.clock_frame)
        self.time_state.pack(side=tk.RIGHT)

        # am
        am_label = tk.Label(master=self.time_state, text="am", font=(self.clock_font, self.am_pm_font_size))
        am_label.pack(side=tk.TOP)

        # pm
        self.pm_label = tk.Label(master=self.time_state, text="pm", font=(self.clock_font, self.am_pm_font_size))
        self.pm_label.pack(side=tk.BOTTOM)

        # will be used to house a cycling button
        self.right_column = tk.Frame(master=self.mid_row, width=self.border_width, bg='blue')
        self.right_column.pack(fill=tk.Y, side=tk.RIGHT)
        self.right_column.pack_propagate(False)

        self.right_btn = tk.Button(master=self.right_column, text=">")
        self.right_btn.pack(side=tk.RIGHT)

        # bottom row
        self.bottom_row = tk.Frame(master=self.clock_face, height=self.border_width)
        self.bottom_row.pack(fill=tk.X, side=tk.BOTTOM)
        self.bottom_row.pack_propagate(False)

        # button section
        self.button_area = tk.Frame(master=self.bottom_row)
        self.button_area.pack(side=tk.BOTTOM)

        self.clock_btn = tk.Button(master=self.button_area, text="Clock")
        self.clock_btn.pack(side=tk.LEFT)

        self.timer_btn = tk.Button(master=self.button_area, text="Timer")
        self.timer_btn.pack(side=tk.LEFT)

        self.stop_watch_btn = tk.Button(master=self.button_area, text="Stop Watch")
        self.stop_watch_btn.pack(side=tk.LEFT)


if __name__ == "__main__":
    app = Digi_Clock()
    app.mainloop()


# alarm sound from pixabay.com link to source:
# https://pixabay.com/sound-effects/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=72117

# fonts from 1001fonts.com link to source:
# https://www.1001fonts.com/digital-fonts.html