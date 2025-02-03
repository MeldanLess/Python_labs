import math

def count_coprime(n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if math.gcd(n, i) == 1:
            count += 1
    return count

if __name__ == '__main__':
    try:
        num = int(input("Введите число: "))
        result = count_coprime(num)
        print(f"Количество чисел, взаимно простых с {num}: {result}")
    except ValueError:
        print("Введите корректное целое число.")
