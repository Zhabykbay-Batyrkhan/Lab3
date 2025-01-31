def is_palindrome(word):
    word = word.replace(" ", "").lower() 
    return word == word[::-1]

word = input("Введи строку: ")
print(is_palindrome(word)) 

