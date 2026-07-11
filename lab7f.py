#!/usr/bin/env python3

# Student ID: sslnu1



class Time:

    def __init__(self, hour=12, minute=0, second=0):

        self.hour = hour

        self.minute = minute

        self.second = second



    def __str__(self):

        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'



    def __repr__(self):

        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'



    def __add__(self, t2):

        return self.sum_times(t2)



    def format_time(self):

        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'



    def sum_times(self, t2):

        return sec_to_time(self.time_to_sec() + t2.time_to_sec())



    def change_time(self, seconds):

        nt = sec_to_time(self.time_to_sec() + seconds)

        self.hour = nt.hour

        self.minute = nt.minute

        self.second = nt.second



    def time_to_sec(self):

        return (self.hour * 60 + self.minute) * 60 + self.second



    def valid_time(self):

        return (

            0 <= self.hour < 24 and

            0 <= self.minute < 60 and

            0 <= self.second < 60

        )




def sec_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t
