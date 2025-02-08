from ascii_utils import count_vowel_consonant_pairs

def task_7_sort_by_vowel_consonant_difference(strings):
    return sorted(strings, key=count_vowel_consonant_pairs)