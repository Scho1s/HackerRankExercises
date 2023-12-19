from math import atan2, degrees

AB, BC = int(input()), int(input())
print(int(round(degrees(atan2(AB, BC)), 0)), u"\u00b0", sep='', end='')
