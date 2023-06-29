"""
# Proje 3
Bu projede ise 4 tane sınıfı oluşturun.

    Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

    Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

    Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

    At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.
"""

class Animal():
    """
    Animal Class
    """
    def __init__(self, specie=None, name=None, number_of_legs=0) -> None:
        print('Animal init fonk.')
        self.specie = specie
        self.name = name
        self.number_of_legs = number_of_legs

    def show_information(self):
        """
        show_information
        :returns: None
        """
        print('show information')

        print(f'specie: {self.specie}\nname: {self.name}\nnumber_of_legs: {self.number_of_legs}')

class Dog(Animal):
    def __init__(self, specie=None, name=None, number_of_legs=0, total = 0) -> None:
        super().__init__(specie, name, number_of_legs)
        self.total = total

    def show_information(self):
        print(f'specie: {self.specie}\nname: {self.name}\nnumber_of_legs: {self.number_of_legs}\ntotal: {self.total}')
    
class Bird(Animal):
    def __init__(self, specie=None, name=None, number_of_legs=0, total = 0) -> None:
        super().__init__(specie, name, number_of_legs)
        self.total = total

    def show_information(self):
        print(f'specie: {self.specie}\nname: {self.name}\nnumber_of_legs: {self.number_of_legs}\ntotal: {self.total}')


class Horse(Animal):
    def __init__(self, specie=None, name=None, number_of_legs=0, total = 0) -> None:
        super().__init__(specie, name, number_of_legs)
        self.total = total

    def show_information(self):
        print(f'specie: {self.specie}\nname: {self.name}\nnumber_of_legs: {self.number_of_legs}\ntotal: {self.total}')


def main():
    """
    Def main
    """
    dog = Dog("Dog","Bob",4,4)
    dir(dog)
    dog.show_information()

    bird = Bird("Bird","Jack",2,9)
    dir(bird)
    bird.show_information()

    horse = Horse("Horse","Fred",2,9)
    dir(horse)
    horse.show_information()


if __name__ == '__main__':
    main()