import math

def digit_sum(n: int) -> int:

    return(sum(int(digit) for digit in str(abs(n))))

def find_divisor_coprime_with_digit_sum(n: int) -> int:
    s = digit_sum(n)
    for i in range(2, n + 1):
        if n % i == 0 and math.gcd(i, s) == 1:
            return i
    return 1

if __name__ == '__main__':
    try:
        num = int(input("Введите число: "))
        divisor = find_divisor_coprime_with_digit_sum(num)
        print(f"Делитель числа {num}, взаимно прсотой с суммой его цифр: {divisor}")
    except ValueError:
        print("Введите корректное целое число.")