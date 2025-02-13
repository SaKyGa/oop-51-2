# декоратор

def my_decorator(func):

    def wrapper():
        print('before func work')
        func()
        print('after func work')

    return wrapper()


@my_decorator
def hello():
    print('hello world!')



# декоратор с аргументом

def repeat(n):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)

        return wrapper
    return decorator


@repeat(3)
def greet():
    print("hello!")

greet()


# декоратор для класса

def class_decorator(cls):

    class NewClass(cls):

        def new_method(self):
            return print("New method")

    return NewClass

@class_decorator
class MyClass:

    def old_method(self):
        return  print("Old method")

obj = MyClass()
obj.old_method()
obj.new_method()


# магические методы

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Bla bla bla !"

# obj = Person('Arsen', 17)
#
# print(obj)



class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        print(f"{self.amount}-----{other.amount}")
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"{self.amount}"

m1 = Money(100)
m2 = Money(300)
m3 = m1 + m2
print(m3)



class Math:

    @staticmethod
    def add( a, b):
        return a + b

print(Math.add(1, 2))



class People:
    count = 0

    def __init__(self, name):
        self.name = name
        People.count += 1

    @classmethod
    def get_population(cls):
        return cls.count

    def test(self):
        pass

    @classmethod
    def create_person(cls, name):
        return cls(name)

person1 = People('Alise')
person2 = People('bob')
person3 = People('Zoos')
print(People.get_population())