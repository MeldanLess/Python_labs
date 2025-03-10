import re

def solve(f):
    with open(f, encoding='utf-8') as file:
        txt = file.read().lower()
        lst = re.findall(r'\b[а-яё]+\b', txt)
        res = sum(1 for w in lst if len(w) > 1 and w[0] == w[-1])
    return res

print(solve("D:\\1_Univer\\Python\\text.txt"))