# class def

class Person:

    # это функция конструктор
    def __init__(self, name, age):

        # атрибуты класса
        self.name = name
        self.age = age

    # self - это ссылка на Obj.
    # метод класса
    def introduce(self,):
        print(f'hi i am {self.name}')

# class Obj. - экземпляр класса
# ardager = Person("Ardager", 25)
#
# ardager.introduce()

# print(type(ardager))
# print(type("Hello"))
# print(type(123))



# родительский класс
class Hero:

    def __init__(self, name, hp, lvl):

        self.name = name
        self.HP = hp
        self.lvl = lvl

    def action(self,):
        print(f"{self.name} делает базовое действие")

naofimo = Hero("NaoFimo", 100, 10)

# дочерний класс
class Shiledhero(Hero):
    pass

naofimo = Shiledhero("NaoFimo", 100, 10)

naofimo.action()




# class -- CamelCase
# переменных, методов, функции -- snake_case