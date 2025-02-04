import re

def find_invalid_dates(text):

    pattern = r"\b(0?[1-9]|[12]\d|3[01])\s+(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s+\d{4}\b"
    matches = re.findall(pattern, text)

    
    invalid_dates = []
    for day, month, year in matches:
        day = int(day)  
        if (month == "февраля" and day > 29) or \
           (month in {"апреля", "июня", "сентября", "ноября"} and day > 30):
            invalid_dates.append(f"{day} {month} {year}")

    return invalid_dates


if __name__ == '__main__':
    text = input("Введите текст: ")
    found_dates = find_invalid_dates(text)

    if found_dates:
        print("Некорректные даты, найденные в тексте:")
        for date in found_dates:
            print(date)
    else:
        print("Некорректные даты не найдены.")
