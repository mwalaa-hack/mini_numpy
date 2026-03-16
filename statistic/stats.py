from core.ndarray import Array
import math

def mean(arr):
    data = arr.flatten().data
    sum = 0
    for x in data:
        sum += x
    return sum / len(data)

def var(arr):
    data = arr.flatten().data
    m = mean(arr)
    sum = 0
    for x in data:
        sum += (x - m) ** 2
    return sum / len(data)

def std(arr):
    v = var(arr)
    return math.sqrt(v)