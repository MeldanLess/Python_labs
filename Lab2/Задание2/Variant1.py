words = input().split()
word_count = {}

for word in words:
    print(word_count.get(word, 0), end=" ")
    word_count[word] = word_count.get(word, 0) + 1



def count_word_occurrences(words):
    
    word_count = {}
    
    for word in words:
        print(word_count.get(word, 0), end=" ")
        word_count[word] = word_count.get(word, 0) + 1

def main():
   
    print("Программа считает, сколько раз каждое слово встречалось ранее в тексте.")
    print("Введите строку с словами через пробел:")
    
    try:
        words = input().strip().split()
        count_word_occurrences(words)
    except Exception as e:
        print(f"\nОшибка: {e}")
    
    input("\n\nНажмите Enter для выхода...")  

if __name__ == "__main__":
    main()
