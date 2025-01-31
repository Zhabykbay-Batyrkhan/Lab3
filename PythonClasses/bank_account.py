class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесено: {amount}, новый баланс: {self.balance}")
        else:
            print("Сумма депозита должна быть положительной!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Снято: {amount}, новый баланс: {self.balance}")
        else:
            print("Недостаточно средств!")

# Пример
account = Account("Иван", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)  # Ошибка, недостаточно средств

'''
Класс Account имеет атрибуты для владельца счета и текущего баланса.
Метод deposit добавляет деньги на счет, если сумма положительная.
Метод withdraw снимает деньги, если на счете достаточно средств.
'''