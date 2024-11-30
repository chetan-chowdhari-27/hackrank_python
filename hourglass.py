#!/bin/python3

import math
import os
import random
import re
import sys

def hour_glass_pattern(arr):
    # Upper half of the hour-glass
    hour_glass = []
    for i in range(4):
        for j in range(4):
            hour_glass.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]) 
    results = max(hour_glass)
    print(results)
            

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    hour_glass_pattern(arr)
