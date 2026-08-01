class Emp:
    def __init__(self,id,name,sal):
        self.__id = id
        self.__name = name
        self.__sal = sal

    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id = __id

    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name = __name

    def getsal(self):
        return self.__sal
    def setsal(self,sal):
        self.__sal = __sal

    def calsal(self):
        finalsal=self.__sal
        print(f'salary:{finalsal}')

    def display(self):
        print(f'ID={self.__id} \t name={self.__name} \t salary={self.__sal}')

    def __str__(self):
        return f'ID={self.__id} \t name={self.__name} \t salary={self.__sal}'   

class Hr(Emp):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.__com = com

    def getcom(self):
        return self.__com
    def setcom(self,com):
        self.__com = com
    
    def display(self):
        print(f'Com:{self.__com}\t',end="")   
        return super().display()   

    def calsal(self):
        finalsal = self.getsal()+self.__com
        print(f'HR salary:{finalsal}')
    def __str__(self):
        return super().__str__()+f'Com:{self.__com}'     

e1 = Hr(101,'Sachin',12122,1000)
# e2 = Emp(18,'Virat',99999)
# e3 = Emp(45,'Rohit',100000)
print(e1)

e1.display()
e1.calsal()
print(e1.getId())
# e2.display()
# e3.display()