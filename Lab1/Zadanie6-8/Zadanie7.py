def count_unique_latin_letters(text):
    return len(set(char.lower() for char in text if char.isalpha() and 'a' <= char.lower() <= 'z'))