def sort_strings_by_word_count():
    n = int(input("Введите количество строк: "))
    strings = [input(f"Введите строку {i + 1}: ") for i in range(n)]
    
    sorted_strings = sorted(strings, key=lambda s: len(s.split()))
    
    print("\nОтсортированные строки по количеству слов:")
    for s in sorted_strings:
        print(s)

if __name__ == "__main__":
    sort_strings_by_word_count()
