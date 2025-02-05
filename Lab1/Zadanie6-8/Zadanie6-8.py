import os

def find_lowercase_letters(text):
    return [char for char in text if char.islower() and char.isalpha()]

def count_unique_latin_letters(text):
    return len(set(char.lower() for char in text if char.isalpha() and 'a' <= char.lower() <= 'z'))

def get_filename_without_extension(path):
    return os.path.splitext(os.path.basename(path))[0]

if __name__ == "__main__":
    while True:
        print("\nВыберите задачу:")
        print("1. Найти все строчные символы латиницы в строке")
        print("2. Найти количество уникальных символов латиницы в строке")
        print("3. Найти имя файла без расширения из пути")
        print("4. Выход")
        
        choice = input("Введите номер задачи: ")
        
        if choice == "1":
            text = input("Введите строку: ")
            result = find_lowercase_letters(text)
            print("Строчные буквы латиницы:", "".join(result) if result else "Не найдено")
        
        elif choice == "2":
            text = input("Введите строку: ")
            result = count_unique_latin_letters(text)
            print(f"Количество уникальных латинских букв: {result}")
        
        elif choice == "3":
            path = input("Введите путь к файлу: ")
            filename = get_filename_without_extension(path)
            print(f"Имя файла без расширения: {filename}")
        
        elif choice == "4":
            print("Выход из программы.")
            break
        
        else:
            print("Ошибка: Введите корректный номер задачи.")
