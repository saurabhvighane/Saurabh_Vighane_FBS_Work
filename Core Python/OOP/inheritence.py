
# sinle level
class Animal:
    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age

    def dispaly(self):
        print(f'Name:{self.name} \t Color:{self.color}\t Age:{self.age}')

class Dog(Animal):
    def __init__(self,name,color,age):
          super().__init__(name,age,color)

a1 = Dog('motya','white',2)
a1.dispaly()

