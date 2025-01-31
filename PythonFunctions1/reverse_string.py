def reverse_words(string):
    words = string.split()
    words.reverse()
    return ' '.join(words)  

string_word = input("Введите строку: ")
print(reverse_words(string_word))
