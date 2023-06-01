#!/usr/bin/env python

class Timekeeper():
    # TODO: improve wording here for clarity
    """
        Object that holds time in seconds. There will be functions to get seconds,
        minutes and hours along with functions to increase and decrease the time by
        any of these units. The boundaries are from 0 to a max of 86399 which is
        a day minus one second.

        The reason for this limitation is to keep things as simple as possible and
        roll over when the timer maxes out. This also applies backwards if the timer
        goes too far back the timer will restart from 86399
    """
    def __init__(self):
        self.second = 1
        self.minute = 60 * self.second
        self.hour = 60 * self.minute # in seconds
        self.day = 24 * self.hour # in seconds

        self.time = 0 # 0 <= time < 86400


    # has the value for time exeded the max? # overflow
    def check_overflow(self):
        if self.time >= self.day:
            self.time = self.time % self.day
    
    # has the value for time gone below zero? # underflow
    def check_underflow(self):
        if self.time < 0:
            self.time = self.day + self.time
            


    def inc_second(self):
        self.time += self.second
        self.check_overflow()
        print(self.time)
    
    def inc_minute(self):
        self.time += self.minute
        self.check_overflow()
        print(self.time)
    
    def inc_hour(self):
        self.time += self.hour
        self.check_overflow()
        print(self.time)


    def dec_second(self):
        self.time -= self.second
        self.check_underflow()
        print(self.time)

    def dec_minute(self):
        self.time -= self.minute
        self.check_underflow()
        print(self.time)

    def dec_hour(self):
        self.time -= self.hour
        self.check_underflow()
        print(self.time)


    def get_seconds(self):
        return f"{str(self.time % self.minute):02}"
    
    def get_minutes(self):
        return f"{str(self.time // self.minute):02}"
    
    def get_hours(self):
        return f"{str(self.time // self.hour):02}"