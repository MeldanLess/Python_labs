from ascii_utils import max_avg_ascii_triplet, quadratic_deviation

def task_11_sort_by_variance_deviation(strings):
    if not strings:
        return []
    reference_weight = max_avg_ascii_triplet(strings[0])
    return sorted(strings, key=lambda s: quadratic_deviation(max_avg_ascii_triplet(s), reference_weight))