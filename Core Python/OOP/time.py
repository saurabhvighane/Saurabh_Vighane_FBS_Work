class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
    def __add__(self,other):
        hr = self.hr+other.hr
        min =self.min+other.min
        sec =self.sec+other.sec
        return Time(hr,min,sec)

    def __str__(self):
        return f'Time: {self.hr}:{self.min}:{self.sec}'

T1 =Time(10,50,20)
T2 =Time(5,20,30)
print(T1+T2)