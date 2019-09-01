# Author:Anthony Quinn
# Date: 30/8/19
# Description:Python classes, creation, use, sub classing, overriding,overloading explained.
# A class can repersent a purpose build, define my own data type.
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honour_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
