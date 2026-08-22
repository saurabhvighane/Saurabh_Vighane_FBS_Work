# 3. Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

def myrange(start, stop, step):

    while start < stop:
        yield start
        start += step


for i in myrange(1, 10, 2):
    print(i)