# 3. Implement two threads to print lowercase and uppercase alphabets concurrently from
# 'a' to 'z' and 'A' to 'Z'.


import threading


def print_lowercase():

    for i in range(ord('a'), ord('z') + 1):
        print(chr(i))


def print_uppercase():

    for i in range(ord('A'), ord('Z') + 1):
        print(chr(i))


t1 = threading.Thread(target=print_lowercase)
t2 = threading.Thread(target=print_uppercase)


t1.start()
t2.start()


t1.join()
t2.join()