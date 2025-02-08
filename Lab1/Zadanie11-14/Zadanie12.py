from ascii_utils import avg_ascii_weight, quadratic_deviation

def task_4_sort_by_quadratic_deviation(strings):
    if not strings:
        return []
    reference_weight = avg_ascii_weight(strings[0])
    return sorted(strings, key=lambda s: quadratic_deviation(avg_ascii_weight(s), reference_weight))