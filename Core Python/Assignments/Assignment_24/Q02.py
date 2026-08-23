# 2. Create two threads, one printing even numbers and the other printing odd numbers
# from 1 to 10. Ensure proper synchronization to alternate between even and odd numbers.

import threading


condition = threading.Condition()

turn = "odd"


def print_odd():
    global turn

    for i in range(1, 11, 2):

        with condition:

            while turn != "odd":
                condition.wait()

            print(i)

            turn = "even"

            condition.notify()


def print_even():
    global turn

    for i in range(2, 11, 2):

        with condition:

            while turn != "even":
                condition.wait()

            print(i)

            turn = "odd"

            condition.notify()


t1 = threading.Thread(target=print_odd)
t2 = threading.Thread(target=print_even)


t1.start()
t2.start()


t1.join()
t2.join()