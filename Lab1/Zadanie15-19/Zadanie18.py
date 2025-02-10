def count_elements_in_segment(arr, a, b):
    return len([x for x in arr if a <= x <= b])