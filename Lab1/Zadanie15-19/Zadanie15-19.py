def find_min_index(arr):
    return arr.index(min(arr))


def count_elements_in_range(arr, a, b):
    return sum(1 for x in arr if a <= x <= b)


def count_elements_between_min(arr):
    min_val = min(arr)
    first = arr.index(min_val)
    last = len(arr) - 1 - arr[::-1].index(min_val)
    return max(0, last - first - 1)


def count_elements_in_segment(arr, a, b):
    return len([x for x in arr if a <= x <= b])


def unique_elements(l1, l2):
    return list(set(l1) ^ set(l2))


def main():
    while True:
        print("\nВыберите задачу:")
        print("1 - Найти индекс минимального элемента")
        print("2 - Найти количество элементов в интервале a..b")
        print("3 - Найти количество элементов между первым и последним минимальным")
        print("4 - Найти количество элементов в отрезке a..b")
        print("5 - Построить список уникальных элементов из двух списков")
        print("0 - Выйти")

        choice = input("Ваш выбор: ")
        
        if choice == "0":
            break
        elif choice == "1":
            arr = list(map(int, input("Введите массив: ").split()))
            print("Индекс минимального элемента:", find_min_index(arr))
        elif choice == "2":
            arr = list(map(int, input("Введите массив: ").split()))
            a, b = map(int, input("Введите границы интервала a b: ").split())
            print("Количество элементов в интервале:", count_elements_in_range(arr, a, b))
        elif choice == "3":
            arr = list(map(int, input("Введите массив: ").split()))
            print("Количество элементов между первым и последним минимальным:", count_elements_between_min(arr))
        elif choice == "4":
            arr = list(map(int, input("Введите массив: ").split()))
            a, b = map(int, input("Введите границы отрезка a b: ").split())
            print("Количество элементов в отрезке:", count_elements_in_segment(arr, a, b))
        elif choice == "5":
            l1 = list(map(int, input("Введите первый список: ").split()))
            l2 = list(map(int, input("Введите второй список: ").split()))
            print("Уникальные элементы:", unique_elements(l1, l2))
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()

