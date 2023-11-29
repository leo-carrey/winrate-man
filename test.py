import math

def find_min_in_array(arr):
    current_min = math.inf
    for number in arr:
        if number < current_min:
            current_min = number
    return current_min

def sort_array(arr: list):
    arr_size = len(arr)
    for _ in range(arr_size):
        current_min = find_min_in_array(arr)
        min_index = arr.index(current_min)
        current_min = arr.pop(min_index)
        arr.insert(0,current_min)
    return arr


import math

def find_min_in_array(arr: list) -> int:
    current_min: int = math.inf
    for number in arr:
        if number < current_min:
            current_min = number
    return current_min

def sort_array(arr: list) -> list:
    arr_size: int = len(arr)
    for _ in range(arr_size):
        current_min: int = find_min_in_array(arr)
        min_index: int = arr.index(current_min)
        current_min = arr.pop(min_index)
        arr.insert(0,current_min)
    return arr