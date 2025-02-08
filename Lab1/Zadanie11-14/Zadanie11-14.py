import statistics

def avg_ascii_weight(s: str) -> float:
    return sum(map(ord, s)) / len(s) if s else 0

def task_2_sort_by_avg_ascii(strings):
    return sorted(strings, key=avg_ascii_weight)

def quadratic_deviation(value, reference):
    return (value - reference) ** 2

def task_4_sort_by_quadratic_deviation(strings):
    if not strings:
        return []
    reference_weight = avg_ascii_weight(strings[0])
    return sorted(strings, key=lambda s: quadratic_deviation(avg_ascii_weight(s), reference_weight))

def count_vowel_consonant_pairs(s):
    vowels = "AEIOUYaeiouyАЕЁИОУЫЭЮЯаеёиоуыэюя"
    consonants = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxzБВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ"
    
    vowel_consonant = sum(1 for i in range(len(s) - 1) if s[i] in vowels and s[i+1] in consonants)
    consonant_vowel = sum(1 for i in range(len(s) - 1) if s[i] in consonants and s[i+1] in vowels)

    return abs(vowel_consonant - consonant_vowel)

def task_7_sort_by_vowel_consonant_difference(strings):
    return sorted(strings, key=count_vowel_consonant_pairs)

def max_avg_ascii_triplet(s):
    if len(s) < 3:
        return 0
    return max(sum(map(ord, s[i:i+3])) / 3 for i in range(len(s) - 2))

def task_11_sort_by_variance_deviation(strings):
    if not strings:
        return []
    reference_weight = max_avg_ascii_triplet(strings[0])
    return sorted(strings, key=lambda s: quadratic_deviation(max_avg_ascii_triplet(s), reference_weight))

def main():
    strings = []
    n = int(input("Введите количество строк: "))
    for i in range(n):
        strings.append(input(f"Введите строку {i + 1}: "))

    print("\nВыберите задачу:")
    print("1 - Сортировка по среднему весу ASCII-кодов символов")
    print("2 - Сортировка по квадратичному отклонению ASCII-кодов")
    print("3 - Сортировка по разнице 'гласная-согласная' и 'согласная-гласная'")
    print("4 - Сортировка по квадратичному отклонению ASCII-кода троек символов")

    choice = input("Введите номер задачи: ")

    if choice == "1":
        sorted_strings = task_2_sort_by_avg_ascii(strings)
    elif choice == "2":
        sorted_strings = task_4_sort_by_quadratic_deviation(strings)
    elif choice == "3":
        sorted_strings = task_7_sort_by_vowel_consonant_difference(strings)
    elif choice == "4":
        sorted_strings = task_11_sort_by_variance_deviation(strings)
    else:
        print("Некорректный выбор")
        return

    print("\nОтсортированные строки:")
    for s in sorted_strings:
        print(s)

if __name__ == "__main__":
    main()
