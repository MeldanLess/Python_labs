import xml.etree.ElementTree as ET  # импортирую модуль для эффективного парсинга XML
import argparse  # импортирую для обработки аргументов командной строки
from collections import Counter  

def count_shops(osm_file):
    counts = Counter()
    # организую итеративный парсинг, чтобы не загружать весь файл в память
    for event, elem in ET.iterparse(osm_file, events=("end",)):
        if elem.tag == 'tag' and elem.attrib.get('k') == 'shop':
            shop_val = elem.attrib.get('v').lower()
            if shop_val != 'supermarket':
                counts[shop_val] += 1
        elem.clear()  # освобождаю память по мере прохода
    return counts  # возвращаю Counter с результатами


def main():
    parser = argparse.ArgumentParser(
        description="Посчитать не супермаркеты в OSM файлах"
    )
    parser.add_argument('osm_files', nargs='+', help='Path(s) to .osm file(s)')
    args = parser.parse_args()

    total_counts = Counter()  # общий счётчик для нескольких файлов
    for path in args.osm_files:
        print(f"Processing {path}...")  # сообщаю, какой файл сейчас
        counts = count_shops(path)  # считаю магазины в текущем файле
        if counts:
            # вывожу результаты по типам
            for shop_type, cnt in counts.items():
                print(f"  {shop_type}: {cnt}")
        else:
            print("  No non-supermarket shops found.")
        total_counts.update(counts)  # аккумулирую в общий счёт

    # если передано несколько файлов, показываю комбинированную статистику
    if len(args.osm_files) > 1:
        print("\nCombined counts:")
        if total_counts:
            for shop_type, cnt in total_counts.items():
                print(f"  {shop_type}: {cnt}")
        else:
            print("  No non-supermarket shops found in any file.")

    # ---- Итоговый отчёт ----
    # считаю общее число магазинов всех типов и сортирую список типов
    total_shops = sum(total_counts.values())
    types = sorted(total_counts.keys())
    print(f"\nВсего магазинов (кроме супермаркетов): {total_shops}")
    print("Типы магазинов:")
    for t in types:
        print(f" - {t}")

if __name__ == '__main__':
    main()