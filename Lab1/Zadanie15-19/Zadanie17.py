def count_elements_between_min(arr):
    min_val = min(arr)
    first = arr.index(min_val)
    last = len(arr) - 1 - arr[::-1].index(min_val)
    return max(0, last - first - 1)