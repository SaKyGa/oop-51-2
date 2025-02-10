# декомпозиция, полиморфизм - инкапсуляция, Абстракция
# @ - декоратор
from abc import ABC, abstractmethod



class OTPService(ABC):

    @abstractmethod
    def sms_send(self):
        pass


class NikitaOTP(OTPService):

    def sms_send(self):
        phone = input("Введите номер тел +996** ** **")


class Animals(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animals):

    def make_sound(self):
        return print("Gaf gaf")

    def move(self):
        return print("run")


dog = Dog()
dog.make_sound()
dog.move()

# модули


from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

