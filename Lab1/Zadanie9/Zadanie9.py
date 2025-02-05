def sort_strings_by_length():
    n = int(input("Введите количество строк: "))
    strings = [input(f"Введите строку {i + 1}: ") for i in range(n)]
    
    sorted_strings = sorted(strings, key=len)
    
    print("\nОтсортированные строки по длине:")
    for s in sorted_strings:
        print(s)

if __name__ == "__main__":
    sort_strings_by_length()
