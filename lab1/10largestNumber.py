import math
def largestNumber(list):
    largest = -math.inf
    for val in list:
        if largest < val:
            largest = val
    return largest

vals = [23,12,34,55,546,345,345,45,656,767,2,345,5,65,6565656,45]
print(largestNumber(vals))