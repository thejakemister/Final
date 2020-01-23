# Course: CS 30
# Period: 4
# Date created: 2020/01/23
# Date last modified: 2020/01/23
# Name: Jacob Leippi
# Description: Final porject, Problem 1


class Time_Conversion:
    # Class for the converion of seconds
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


def TIME():
    # function for converting seconds into hours minutes and seconds
    seconds = int((input("Enter the amount of seconds: ")))
    hours = seconds // 3600
    seconds = seconds - hours * 3600
    minutes = seconds // 60
    seconds = seconds - minutes * 60
    Time = Time_Conversion(hours,  minutes, seconds)
    print(str(Time.hours) + " hours " + str(Time.minutes) + " minutes " +
    str(Time.seconds) + " seconds ")


TIME()
# Calls the function to convert the seconds into hours, minutes, and seconds
