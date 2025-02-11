def check_numbers(numbers):
    
    seen = set()
    for num in numbers:
        if num in seen:
            print("YES")
        else:
            print("NO")
            seen.add(num)

def main():
    
    print("Программа проверяет, встречались ли числа раньше.")
    print("Введите последовательность чисел через пробел:")
    
    try:
        numbers = input().strip().split()
        check_numbers(numbers)
    except Exception as e:
        print(f"Ошибка: {e}")
        
if __name__ == "__main__":
    main()