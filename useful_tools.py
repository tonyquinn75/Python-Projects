# Author:Anthony Quinn
# Date: 30/8/19
# This file will be used/imported into the modules_and_pip pytthon file to demonstrate how imported file functionality/data can be used.
import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)
