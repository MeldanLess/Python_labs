import re

def d(s):
    p = re.compile(r'^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$')
    m = p.match(s)
    if not m:
        return False
    dd, mm, yy = map(int, s.split('/'))
    if mm in (1, 3, 5, 7, 8, 10, 12): #январь, март, май, июль, август, октябрь, декабрь
        mxd = 31
    elif mm in (4, 6, 9, 11): #апрель, июнь, сентябрь, ноябрь
        mxd = 30
    elif mm == 2: #февраль
        mxd = 29 if (yy % 4 == 0 and (yy % 100 or yy % 400 == 0)) else 28 #Если год кратен 4, и либо не кратен 100, либо кратен 400, то год считается високосным
    else:
        return False
    return 1 <= dd <= mxd

def c(s):
    if not d(s):
        raise ValueError("Некорректный аргумент")
    return s

s = input("Дата (DD/MM/YYYY): ")
try:
    print("Дата:", c(s))
except Exception as e:
    print(e)
