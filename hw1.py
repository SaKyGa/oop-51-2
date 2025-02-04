# Задание 1: Создание класса Hero
#   1) Создайте класс Hero с атрибутами:
#
#      * name — имя.
#      * lvl — уровень.
#      * HP — количество жизни.
#   2) Добавьте метод introduce, который выводит информацию о герое в формате:
#   \\\"Привет, меня зовут <Имя>, мой lvl <уровень> , мое HP <HP>\\\".
#
#   3) Создайте экземпляр класса Hero и вызовите метод introduce.
#
# Задание 2: Методы класса
#   1) В классе Hero добавьте метод is_adult, который проверяет, является ли герой уровнем
#   выше 10. Если уровень больше или равен 10, метод должен возвращать True, иначе — False.
#
#   2) Создайте несколько экземпляров класса Hero с разными уровнями и вызовите
#   метод is_adult для каждого.
#
# Задание 3: Репозиторий GItHub.
#   1) Создать репозиторий OOP-50-2
#
#   2) Привязать ваше домашнее задание к репозиторию OOP-50-2
#   3) сделать комит и залить ваше ДЗ на ваш репозиторий OOP-50-2
#
#   4) Прикрепить ссылку на ваше ДЗ

class MainHero:

    def __init__(self, name, hp, lvl):

        self.name = name
        self.hp = hp
        self.lvl = lvl

    def is_adult(self):
        return self.lvl >= 10

    def introduce(self,):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl} , мое HP {self.hp}")

class SecondaryHero(MainHero):

    def __init__(self, name, hp, lvl):
        super().__init__(name, hp, lvl)


nana = SecondaryHero("Nana", 7889, 75)

nana.introduce()

gesen = SecondaryHero("Gesen", 6631, 34)

gesen.introduce()

masha = SecondaryHero("Masha", 10678, 9)

masha.introduce()

print(f"{nana.name} уревень выше 10?{nana.is_adult()}")
print(f"{gesen.name} уревень выше 10?{gesen.is_adult()}")
print(f"{masha.name} уревень выше 10?{masha.is_adult()}")