#!/usr/bin/env python
# ^ this should work fine in a virtual environment

import tkinter as tk

window = tk.Tk()
window.geometry('200x150')

border_width = 20
overall_font = 0
clock_font = "Arial" # placeholder
time_font_size = 35
am_pm_font_size = 20
current_time = "12:34"
isAm = True
title = "April 3, 2023" # placeholder

# Digital clock face is contained here
clock_face = tk.Frame(master=window, width=200, height=150)
clock_face.pack(fill=tk.BOTH, expand=True)
clock_face.pack_propagate(False)

# top row
top_row = tk.Frame(master=clock_face, height=border_width)
top_row.pack(fill=tk.X, side=tk.TOP)

# date/other
title_label = tk.Label(master=top_row, text=title)
title_label.pack(side=tk.TOP)

# middle row
mid_row = tk.Frame(master=clock_face)
mid_row.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
mid_row.pack_propagate(False)

# will be used to house a cycling button
left_column = tk.Frame(master=mid_row, width=border_width, bg='blue')
left_column.pack(fill=tk.Y, side=tk.LEFT)
left_column.pack_propagate(False)

left_btn = tk.Button(master=left_column, text="<")
left_btn.pack(side=tk.LEFT)


# holds the actual clock display (numbers + am/pm)
clock_frame = tk.Frame(master=mid_row, bg="yellow")
clock_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
clock_frame.pack_propagate(False)

# clock time
clock_time = tk.Label(master=clock_frame, text=current_time, font=(clock_font, time_font_size))
clock_time.pack(side=tk.LEFT)

# time state
time_state = tk.Frame(master=clock_frame)
time_state.pack(side=tk.RIGHT)
# am
am_label = tk.Label(master=time_state, text="am", font=(clock_font, am_pm_font_size))
am_label.pack(side=tk.TOP)

# pm
pm_label = tk.Label(master=time_state, text="pm", font=(clock_font, am_pm_font_size))
pm_label.pack(side=tk.BOTTOM)

# will be used to house a cycling button
right_column = tk.Frame(master=mid_row, width=border_width, bg='blue')
right_column.pack(fill=tk.Y, side=tk.RIGHT)
right_column.pack_propagate(False)

right_btn = tk.Button(master=right_column, text=">")
right_btn.pack(side=tk.RIGHT)

# bottom row
bottom_row = tk.Frame(master=clock_face, height=border_width)
bottom_row.pack(fill=tk.X, side=tk.BOTTOM)
bottom_row.pack_propagate(False)

# button section
button_area = tk.Frame(master=bottom_row)
button_area.pack(side=tk.BOTTOM)

clock_btn = tk.Button(master=button_area, text="Clock")
clock_btn.pack(side=tk.LEFT)

timer_btn = tk.Button(master=button_area, text="Timer")
timer_btn.pack(side=tk.LEFT)

stop_watch_btn = tk.Button(master=button_area, text="Stop Watch")
stop_watch_btn.pack(side=tk.LEFT)


window.mainloop()

# alarm sound from pixabay.com link to source:
# https://pixabay.com/sound-effects/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=72117

# fonts from 1001fonts.com link to source:
# https://www.1001fonts.com/digital-fonts.html