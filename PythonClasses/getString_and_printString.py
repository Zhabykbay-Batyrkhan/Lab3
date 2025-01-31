class MyClass:
    def __init__(self):
        self.input_string = ""
    
    def getString(self):
        self.input_string = input("Введите строку: ") 
    
    def printString(self):
        print(self.input_string.upper())

obj = MyClass()
obj.getString()
obj.printString()

'''
Метод getString запрашивает строку у пользователя и сохраняет её в атрибуте input_string.
Метод printString выводит строку в верхнем регистре с помощью метода upper()
'''