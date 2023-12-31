#!/bin/python3

import math
import os
import random
import re
import sys


class Car:
    def __init__(self, speed, units):
        self.speed = speed
        self.units = units

    def __repr__(self):
        return f"{__class__.__name__} with the maximum speed of {self.speed} {self.units}"

class Boat:
    def __init__(self, speed):
        self.speed = speed

    def __repr__(self):
        return f"{__class__.__name__} with the maximum speed of {self.speed} knots"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        print("%s\n" % vehicle)
    #     fptr.write("%s\n" % vehicle)
    # fptr.close()
