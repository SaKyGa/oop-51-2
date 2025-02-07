# Наследование:
#   - В директории HomeWorks создайте файл hw2.py
#   - В файле hw2.py создайте родительский класс Heroes.
#   - В классе Heroes создайте следующие методы и атрибуты:
#       * name - атрибут
#       * hp - атрибут
#       * action - метод ( что будет делать этот метод на ваше усмотрение )
#       * attack - метод ( что будет делать этот метод на ваше усмотрение )
#   - В этом же файле hw2.py создайте дочерний класс Archer, который наследуется от Heroes.
# Полиморфизм:
#   - В классе Archer должны быть свои: Атрибуты arrows (количество стрел) и precision (точность).
#   - Измение метод attack, который теперь будет уменьшает количество стрел на 1 и выводит сообщение об успешной
#   или неудачной атаке в зависимости от точности.
#   - Добавьте новый метод rest, который добавляет 5 стрел и выводит сообщение о пополнении стрел.
#   - Добавьте новый метод status, который возвращает информацию о текущем состоянии персонажа (имя, здоровье и любые уникальные атрибуты для подклассов).
#   - Создайте экземпляр класса и вызовите его методы
import random



class Heroes:

    def __init__(self, name, hp, lvl):

        self.name = name
        self.hp = hp
        self.lvl = lvl

    def action(self):
        print(f"{self.name} Атакует врага!")

    def attack(self):
        print(f"{self.name} Нанес урон по врагу!")


class Archer(Heroes):

    def __init__(self, name="Mia", lvl= 67, hp=100, arrows=15, precision=70):
        super().__init__(name, hp, lvl)
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.arrows = arrows
        self.precision = precision
        self.crit_attack = 3

    def attack(self):
        if self.arrows <= 0:
            print(f"{self.name} Пытается атаковать НО СТРЕЛ НЕ ОСТАЛОСЬ!")
            return

        self.arrows -= 1
        hit_chance = random.randint(1,100)

        if hit_chance <= self.precision:
            is_crit = random.randint(1, 100) <= 75
            damage = 25 * self.crit_attack if is_crit else 23
            crit_text = "!!!Крит Удар!!!" if is_crit else  ""
            print(f"{self.name} атакует! Успешно! Урон{damage}. {crit_text}\nОсталось стрел: {self.arrows}")
        else:
            print(f"{self.name} атакует! Неудачно...\nОсталось стрел: {self.arrows}")

    def rest(self):
        self.arrows += 5
        print(f"Пополнение стрел \nОсталось стрел: {self.arrows}")

archer = Archer()

while True:
    action = input("Введите ('attack', 'rest', 'exit') для действия: ").strip().lower()

    if action == "attack":
        if not archer.attack() and archer.arrows == 0:
            print("Стрел не осталось! Введите 'rest' для перезарядки!")

    elif action == "rest":
        archer.rest()

    elif action == "exit":
        print("Бой окончен!")
        break

    else:
        print("Введите одно из действий ('attack', 'rest', 'exit')")

