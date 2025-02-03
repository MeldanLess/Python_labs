def task2_check_order():

    s = input("Введите строку (латинские символы): ")
    lower_chars = ''.join([c for c in s if c.islower()])
    if lower_chars == ''.join(sorted(lower_chars)):
        print("Строчные символы упорядочены по возрастанию.")
    else:
        print("Строчные символы НЕ упорядочены по возрастанию.")