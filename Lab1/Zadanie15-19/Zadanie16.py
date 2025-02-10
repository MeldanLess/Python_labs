def count_elements_in_range(arr, a, b):
    return sum(1 for x in arr if a <= x <= b)