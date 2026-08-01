class Emp:
    def __init__(self,id,name,sal):
        self.__id = id
        self.__name = name
        self.__sal = sal

    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id = id

    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name = name

    def getsal(self):
        return self.__sal
    def setsal(self,sal):
        self.__sal = sal

    def display(self):
        print(f'ID={self.__id} \t name={self.__name} \t salary={self.__sal}')

class HR(Emp):
    def __init__(self,id,name,sal,com=1000):
        super().__init__(id,name,sal)
        self.__com = com

    def getcom(self):
        return self.__com
    def setcom(self,com):
        self.__com = com
    def display(self):
        print(f'Com:{self.__com}\t',end="")     
        return super().display()   

e1 = HR(101,'Sachin',12122)
e1.display()