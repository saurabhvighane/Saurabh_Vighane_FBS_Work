def recursive():
    print("Yare! Yare!")
    recursive1()

def recursive1():
    print("Baka!")
    recursive2()

def recursive2():
    print("Dattebayo!")
    recursive()
recursive()