# Завдання 1
# Створіть клас Message з атрибутами
#  user – ім’я автора повідомлення
#  text – текст повідомлення
#  time – час повідомлення(використайте модуль datetime)
# приклад datetime.strptime('10:23', '%H:%M')
# методи:
#  __str__(self) – повертає текст повідомлення та час
#  __len__(self) – повертає довжину повідомлення
#  __gt__(self, other) – перевіряє чи є повідомлення self
# старішим за other
# Створіть список з декількома повідомленнями та виведіть
# його. Відсортуйте список і знову виведіть

# import datetime as d
#
# class Message:
#     def __init__(self, user:str,text:str,time:str):
#         self._user = user
#         self._text = text
#         self._time = d.datetime.strptime(time,"%H:%M")
#
#     def __str__(self):
#         return f"User: {self._user}, Text: {self._text}. [{self._time}]"
#
#     def __len__(self):
#         return len(self._text)
#
#     def __gt__(self, other):
#         return self._time > other._time
#
#
# mes = Message("Bob", "Hi world", "11:11")
# mes1 = Message("Bob", "Hello world", "11:15")
# print(mes)
# print(len(mes))
# print(mes>mes1)
#
# messages =[]
# messages.append(Message("Bob", "Hi wqwwqd", "11:23"))
# messages.append(Message("Bob", "Hi woqwrld", "11:11"))
# messages.append(Message("Bqwob", "Hi wqqwworld", "12:11"))
# messages.append(Message("Bqweob", "Hi qwqeqworld", "15:11"))
# messages.append(Message("qwBob", "Hi wqwqworld", "1:11"))
#
#
# messages.sort()
# for message in messages:
#     print(message)

# Завдання 2
# Створіть клас Song з атрибутами
#  name – назва пісні
#  author – ім’я автора
# Практичне завдання
# методи:
#  __eq__(self, other) – перевіряє чи дві пісні однакові
#  __str__(self, other) – повертає рядок з назвою та автором
# Створіть клас Playlist з атрибутами
#  songs – список пісень(об’єкти класу Song)
# методи:
#  __len__(self) – повертає кількість пісень
#  __contains__(self, item) – перевіряє чи є пісня в плейлисті
#  __iter__(self) – повертає літератор для циклу for
#  add_song(self, song) – додає пісню в плейлист
#  remove_song(self, song) – видаляє пісню з плейлиста
# Створіть порожній плейлист
# Створіть 3 пісні:
# "Imagine", "John Lennon"
# "Bohemian Rhapsody", "Queen"
# "Shape of You", "Ed Sheeran"
# Добавте їх в плейлист
# Пройдіться циклом for по плейлисту та виведіть кожну
# пісню на екран

# class Song:
#     def __init__(self, name:str, author:str):
#         self._name = name
#         self._author = author
#
#     def __gt__(self, other):
#         return self._name > other._name and self._author > other._author
#
#
#     def __str__(self):
#         return f"Песня: - {self._name} [Автор:{self._author}]"
#
# music1 = Song("Du hast", "Rammstein")
# music2 = Song("Imagine", "John Lennon")
# music3 = Song("Bohemian Rhapsody", "Queen")
# music4 = Song("Shape of You", "Ed Sheeran")
# music5 = Song("Mather", "Rammstein")
# print(music1 == music2)
# print(music1)
#
# class PlayList:
#     def __init__(self,songs: list):
#         self._songs = songs
#
#     def __len__(self):
#         return len(self._songs)
#
#     def __contains__(self, item):
#         return item in self._songs
#
#     def __iter__(self):
#         return iter(self._songs)
#
#     def add_song(self,song: Song):
#         self._songs.append(song)
#
#     def remove_song(self,song: Song):
#         if song in self._songs:
#             self._songs.remove(song)
#         else:
#             raise KeyError
#
# playlist = PlayList([music1,music2,music3,music4])
# playlist.add_song(music5)
# playlist.remove_song(music1)
#
# print("Количество песен: ",len(playlist))
# for song in playlist:
#     print(song)
# print(music2 in playlist)

# Завдання 3
# Створіть клас Cart з атрибутами
#  items – список товарів
#  total – загальна ціна товарів
# методи:
#  __str__(self) – повертає рядок зі списком товарів
#  __len__(self) – повертає кількість товарів
#  __add__(self, other) – об’єднує 2 кошики та повертає
# новий кошик
# Створіть два кошики. Виведіть кількість товарів в кожному
# з них. Виведіть самі кошики. Об’єднайте їх та виведіть
# кількість товарів в новому кошику та товари в ньому
#
class Cart:
    def __init__(self, items: list, total: int):
        self._items = items
        self._total = total

    def __str__(self):
        return f'items: {self._items}, total: {self._total}'

    def __len__(self):
        return len(self._items)

    def __add__(self, other):
        if not  isinstance(other, Cart):
            raise TypeError

        new_cart = self._items + other._items
        new_total = self._total + other._total
        return Cart(new_cart, new_total)

    def __contains__(self, item):
        return item in self._items

cart1 = Cart(["Хлеб", "Соль", "Рис"], 45)
cart2 = Cart(["Молоко", "Мясо"], 24)
print(cart1)
print("Длина 2 набора: ",len(cart2))
cart3 = cart1+cart2
print(cart3)
print("Хлеб" in cart2)

