# 1. We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def Fibonacci(no):
        a=0
        b=1

        while a<=no:
            yield(a)
            c=a+b
            a=b
            b=c
    
no=int(input("Enter limit: "))
for i in Fibonacci(no):
    print(i)
    