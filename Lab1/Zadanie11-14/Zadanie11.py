from ascii_utils import avg_ascii_weight

def task_2_sort_by_avg_ascii(strings):
    return sorted(strings, key=avg_ascii_weight)