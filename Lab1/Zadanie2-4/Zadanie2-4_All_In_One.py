def task2_check_order():

    s = input("Введите строку (латинские символы): ")
    lower_chars = ''.join([c for c in s if c.islower()])
    if lower_chars == ''.join(sorted(lower_chars)):
        print("Строчные символы упорядочены по возрастанию.")
    else:
        print("Строчные символы НЕ упорядочены по возрастанию.")


def task10_count_A():


    s = input("Введите строку: ")
    count = s.count("A")
    print(f"Количество букв 'A': {count}")


def task17_file_name():
    
    path = input("Введите путь к файлу: ")
    last_slash = max(path.rfind('/'), path.rfind('\\'))
    if last_slash != -1:
        file_name = path[last_slash+1:]
    else:
        file_name = path
    dot_index = file_name.rfind('.')
    if dot_index != -1:
        file_name_without_ext = file_name[:dot_index]
    else:
        file_name_without_ext = file_name
    print(f"Имя файла без расширения: {file_name_without_ext}")


def main():
    
    print("Выберите задачу для решения:")
    print("2  - Проверка упорядоченности строчных символов")
    print("10 - Подсчёт количества букв 'A'")
    print("17 - Извлечение имени файла без расширения")
    choice = input("Введите номер задачи (2, 10, 17): ")

    if choice == '2':
        task2_check_order()
    elif choice == '10':
        task10_count_A()
    elif choice == '17':
        task17_file_name()
    else:
        print("Неверный выбор. Попробуйте ещё раз.")


if __name__ == '__main__':
    main()
