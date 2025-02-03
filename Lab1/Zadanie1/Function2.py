def sum_digits_divisible_by_3(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)) if int(digit) % 3 ==0)

if __name__ == '__main__':
    try:
        num = int(input("Введите число: "))
        result = sum_digits_divisible_by_3(num)
        print(f"Сумма цифр, делящихся на 3 в числе {num}: {result}")
    except ValueError:
        print("Введите корректное целое число.")