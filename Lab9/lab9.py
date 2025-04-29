import pandas as pd
import re
from datetime import timedelta

def parse_time(s: str) -> timedelta:
    s = str(s)
    h = int(re.search(r'(\d+)\s*ч',    s).group(1)) if re.search(r'(\d+)\s*ч',    s) else 0
    m = int(re.search(r'(\d+)\s*мин',  s).group(1)) if re.search(r'(\d+)\s*мин',  s) else 0
    sec = int(re.search(r'(\d+)\s*сек', s).group(1)) if re.search(r'(\d+)\s*сек', s) else 0
    return timedelta(hours=h, minutes=m, seconds=sec)

# 1. читаем оба файла (при желании можно объединить их через pd.concat)
df1 = pd.read_csv('14 - 1.csv', sep=',', quotechar='"')
df2 = pd.read_csv('14 - 2.csv', sep=',', quotechar='"')
df = pd.concat([df1, df2], ignore_index=True)

# 2. преобразуем оценки
df['Score'] = df['Оценка/10,00'].str.replace(',', '.').astype(float)

# 3. парсим время
df['TimeDelta'] = df['Затраченное время'].apply(parse_time)

# 4. задаём порог
threshold_str = '21 мин. 0 сек.'   # поменяйте при необходимости
threshold = parse_time(threshold_str)

# 5. фильтруем
filtered = df[(df['TimeDelta'] > threshold) & (df['Score'] == 9.0)]

# 6. выводим
print(f"Пороговое время: {threshold_str}")
print(f"Найдено участников: {len(filtered)}\n")
print(filtered[['Фамилия', 'Имя', 'Затраченное время', 'Оценка/10,00']].to_string(index=False))
