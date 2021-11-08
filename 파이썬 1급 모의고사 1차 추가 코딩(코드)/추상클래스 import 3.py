from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("두 발로 움직입니다")
        
class Dog(Animal):
    def move(self):
        print("네 발로 움직입니다")

h=Human()
h.move()

d=Dog()
d.move()



'''
class Human(Animal):
    def run(self):
        print("두 발로 움직입니다")
        '''
