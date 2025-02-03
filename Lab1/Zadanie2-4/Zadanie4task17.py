def task17_file_name():
    
    path = input("Введите путь к файлу: ")
    last_slash = max(path.rfind('/'), path.rfind('\\'))
    if last_slash != -1:
        file_name = path[last_slash+1:]
    else:
        file_name = path
    dot_index = file_name.rfind('.')
    if dot_index != -1:
        file_name_without_ext = file_name[:dot_index]
    else:
        file_name_without_ext = file_name
    print(f"Имя файла без расширения: {file_name_without_ext}")