from abc import ABC,abstractmethod
class Emp(ABC):
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal

    @abstractmethod
    def calsal(self):
        print(f'Emp salary{self.sal}')

    def getId(self):
        return self.id
    def setId(self,id):
        self.id = id

    def getname(self):
        return self.name
    def setname(self,name):
        self.name = name

    def getsal(self):
        return self.sal
    def setsal(self,sal):
        self.sal = sal

    def display(self):
        print(f'ID={self.id} \t name={self.name} \t salary={self.sal}')

class HR(Emp):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.__com = com
    def calsal(self):
        finalsal=self.getsal()+self.__com
        print(f'Final sal:{finalsal}')

    def getcom(self):
        return self.com
    def setcom(self,com):
        self.__com = com
    def display(self):
        print(f'Com:{self.__com}\t',end="")     
        return super().display()   

e1 = HR(101,'Sachin',12122,1000)
e1.display()
e1.calsal()