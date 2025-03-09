import sys

# Читаем входные данные
n, k, m = map(int, sys.stdin.readline().split())
tariffs = []  # Сюда сложим все тарифные планы

tariffs_by_day = [[] for _ in range(n)]  # Для каждого дня храним список тарифов

# Считываем тарифные планы и раскидываем их по дням
for _ in range(m):
    l, r, c, p = map(int, sys.stdin.readline().split())
    for day in range(l - 1, r):  # Дни хранятся с 1, а индексы с 0, так что -1
        tariffs_by_day[day].append((p, c))  # Добавляем кортеж (цена, количество ядер)

# Сюда будем складывать общую сумму
total_cost = 0

# Обрабатываем каждый день
for day in range(n):
    tariffs_by_day[day].sort()  # Сортируем тарифы по цене, чтобы хватать самое дешёвое
    remaining = k  # Столько ядер нужно на этот день
    day_cost = 0  # Стоимость за текущий день
    
    # Бежим по тарифам, пока не наберем нужное количество ядер
    for price, cores in tariffs_by_day[day]:
        if remaining <= 0:
            break  # Если уже набрали, дальше не идём
        take = min(remaining, cores)  # Берем столько, сколько надо (или сколько дают)
        day_cost += take * price  # Считаем стоимость
        remaining -= take  # Уменьшаем оставшееся кол-во ядер
    
    if remaining > 0:
        print(-1)  # Если ядер не хватило, всё, конец игры
        sys.exit(0)
    
    total_cost += day_cost  # Добавляем к общей стоимости

print(total_cost)  # Выводим ответ
