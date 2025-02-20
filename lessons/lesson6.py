# Множественное наследование

# горизонтальное наследование
class Flyable:

    def fly(self):
        return 'Летит'


class Swimmable:

    def swim(self):
        return 'Плавает'


class Duck(Flyable, Swimmable):

    def make_sound(self):
        return 'Кря-Кря!!'

donald_duck = Duck()
print(donald_duck.fly())
print(donald_duck.swim())

# ромбовидное наследование

class Animal:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Издает звук"

    def action(self):
        return 'Базовое действие'


class Swimmable(Animal):

    def action(self):
        return 'Плавает'


class Flyable(Animal):

    def action(self):
        return 'Летит'


class Duck(Swimmable, Flyable):

    def make_sound(self):
        return 'Кря-Кря!!'

    def action(self):
        return 'Летает и плавает'

#
# donald_duck = Duck
# print(donald_duck.action)
# print(Duck.mro)