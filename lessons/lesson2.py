# декомпозиция, полиморфизм - инкапсуляция

class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"base action")

class Warrior(Hero):

    def __init__(self, name="Jonson", lvl= 1, hp=100, st=50):
        super().__init__(name, hp, lvl)
        self.st = st
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} action")

    def about_us(self):
        print(f"Name: {self.name} ")

kirrito = Warrior(lvl=5, hp =1000, st=100, name="Kirrito")

kirrito.action()
kirrito.about_us()



