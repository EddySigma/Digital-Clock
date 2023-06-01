import tkinter as tk
from Timekeeper import Timekeeper



class Timer(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # TODO: move settings out of here
        self.clock_font = "Arial" # placeholder
        self.time_font_size = 28

        # variable to hold time
        self.time = Timekeeper()

        # holder for everything
        self.timer_frame = tk.Frame(master=container)
        self.timer_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.timer_frame.pack_propagate(False)

        self.timer_frame.columnconfigure([0,2,4], weight=3)
        self.timer_frame.columnconfigure(5, weight=2)

        self.timer_frame.rowconfigure([0,2], weight=1)
        self.timer_frame.rowconfigure(1, weight=3)


        """
        Note: sticky uses n-e-s-w as in north, east, south and west. They indicate
        in what direction the item (in this case a button) will stick to think of
        it as a number pad where the bottom left is 1 and top right is 9 (like a 
        keyboard) n=8,e=6,s=2,2=4. They can be combined too such as ne=9,se=3 etc.
        Other important combinations are ew => stick from left to right and ns =>
        stick from top to bottom and nesw => stick to everything around
        """
        
        # top row of buttons to increase time in h/m/s
        self.inc_hour = tk.Button( # inc -> increase
            master=self.timer_frame,
            text='\u23F6', # '\u23F6' special character triangle pointing up
            command=self.time.inc_hour) 
        self.inc_hour.grid(
            column=0, 
            row=0, 
            sticky='nesw')
        
        self.inc_minute = tk.Button(
            master=self.timer_frame,
            text='\u23F6', 
            command=self.time.inc_minute)
        self.inc_minute.grid(
            column=2, 
            row=0, 
            sticky='nesw')
        
        self.inc_second = tk.Button(
            master=self.timer_frame, 
            text='\u23F6',
            command=self.time.inc_second)
        self.inc_second.grid(
            column=4, 
            row=0, 
            sticky='nesw')

        # label row to inform user of hh:mm:ss
        # TODO: look into using hints to display what these are... Why?... Why Not?
        
        # time labels for hh:mm:ss
        self.timer_hour_lbl = tk.Label(
            master=self.timer_frame, 
            text=self.time.get_hours(), 
            font=(self.clock_font, self.time_font_size))
        self.timer_hour_lbl.grid(column=0, row=1)

        self.hour_min_div_lbl = tk.Label(
            master=self.timer_frame, 
            text=":", 
            font=(self.clock_font, self.time_font_size))
        self.hour_min_div_lbl.grid(column=1, row=1)

        self.timer_minute_lbl = tk.Label(
            master=self.timer_frame, 
            text=self.time.get_minutes(), 
            font=(self.clock_font, self.time_font_size))
        self.timer_minute_lbl.grid(column=2, row=1)

        self.m_s_div_lbl = tk.Label(
            master=self.timer_frame, 
            text=":", 
            font=(self.clock_font, self.time_font_size))
        self.m_s_div_lbl.grid(column=3, row=1)
        
        self.timer_second_lbl = tk.Label(
            master=self.timer_frame, 
            text=self.time.get_seconds(), 
            font=(self.clock_font, self.time_font_size))
        self.timer_second_lbl.grid(column=4, row=1)

        
        # bottom button row for hh:mm:ss
        self.dec_hour_btn = tk.Button(
            master=self.timer_frame, 
            text='\u23F7',  # '\u23F7' special character triangle pointing down
            command=self.time.dec_hour)
        self.dec_hour_btn.grid(column=0, row=2, sticky='nesw') # dec -> decrease

        self.dec_minute_btn = tk.Button(
            master=self.timer_frame, 
            text='\u23F7',
            command=self.time.dec_minute)
        self.dec_minute_btn.grid(column=2, row=2, sticky='nesw')

        self.dec_second_btn = tk.Button(
            master=self.timer_frame, 
            text='\u23F7', 
            command=self.time.dec_second)
        self.dec_second_btn.grid(column=4, row=2, sticky='nesw')
        
        # control buttons area
        
        self.control_btns_frame = tk.Frame(master=self.timer_frame)
        self.control_btns_frame.grid(column=5, row=0, rowspan=3, sticky="ew")
        self.control_btns_frame.columnconfigure(0, weight=1)
        
        # buttons
        self.start_btn = tk.Button(
            master=self.control_btns_frame, 
            text="Start",
            command=self.start_click)
        self.start_btn.grid(column=0, row=0, sticky="ew")

        self.stop_btn = tk.Button(
            master=self.control_btns_frame,
            text="Stop",
            command=self.stop_click)
        self.stop_btn.grid(column=0, row=1, sticky="ew")

        self.clear_btn = tk.Button(
            master=self.control_btns_frame, 
            text="Clear",
            command=self.clear_click)
        self.clear_btn.grid(column=0, row=2, sticky="ew")

    # ===== actions for the control buttons for the timer =====
    def start_click(self):
        self.start_btn['state'] = 'disabled'
        self.stop_btn['state'] = 'normal'
        self.clear_btn['state'] = 'normal'
        
        # disable time buttons
        self.inc_hour['state'] = 'disabled'
        self.inc_minute['state'] = 'disabled'
        self.inc_second['state'] = 'disabled'
    
    def stop_click(self):
        self.start_btn['state'] = 'normal'
        self.stop_btn['state'] = 'disabled'
    
    def clear_click(self):
        self.start_btn['state'] = 'normal'
        self.stop_btn['state'] = 'disabled'
        self.clear_btn['state'] = 'disabled'
        
        # enable time buttons
        self.inc_hour['state'] = 'normal'
        self.inc_minute['state'] = 'normal'
        self.inc_second['state'] = 'normal'