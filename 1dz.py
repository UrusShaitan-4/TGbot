# Завдання 1
# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька рахунків, добавте їх у список та для
# кожної викличте відповідні методи.


class CreditCardPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата картой: {amount} {self.currency}")


class PayPalPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата PayPal: {amount} {self.currency}")


class CryptoPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"Оплата криптокошельком: {amount} {self.currency}")


def create_payment():
    print("\nВыберите тип оплаты:")
    print("1 - Credit Card")
    print("2 - PayPal")
    print("3 - Crypto")

    choice = input("Введите номер: ")
    curr = input("Введите валюту (например, USD или UAH): ")

    if choice == "1":
        return CreditCardPayment(curr)
    elif choice == "2":
        return PayPalPayment(curr)
    elif choice == "3":
        return CryptoPayment(curr)
    else:
        print("Ошибка выбора, попробуем еще раз.")
        return None


payment1 = create_payment()
payment2 = create_payment()
payment3 = create_payment()

payments_list = [payment1, payment2, payment3]

print("\nРезультаты оплаты:")
if payments_list[0]: payments_list[0].pay(100)
if payments_list[1]: payments_list[1].pay(250)
if payments_list[2]: payments_list[2].pay(500)