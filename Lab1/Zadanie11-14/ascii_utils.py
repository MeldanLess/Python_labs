import statistics

def avg_ascii_weight(s: str) -> float:
    return sum(map(ord, s)) / len(s) if s else 0

def quadratic_deviation(value, reference):
    return (value - reference) ** 2

def count_vowel_consonant_pairs(s):
    vowels = "AEIOUYaeiouyАЕЁИОУЫЭЮЯаеёиоуыэюя"
    consonants = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxzБВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ"
    
    vowel_consonant = sum(1 for i in range(len(s) - 1) if s[i] in vowels and s[i+1] in consonants)
    consonant_vowel = sum(1 for i in range(len(s) - 1) if s[i] in consonants and s[i+1] in vowels)
    
    return abs(vowel_consonant - consonant_vowel)

def max_avg_ascii_triplet(s):
    if len(s) < 3:
        return 0
    return max(sum(map(ord, s[i:i+3])) / 3 for i in range(len(s) - 2))