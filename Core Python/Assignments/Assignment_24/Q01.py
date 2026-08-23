# 1. Calculate the sum of squares of numbers from 1 to 100 using four threads. Divide the
# range equally among the threads, and each thread calculates the sum of squares for its
# range. Finally, combine the results to get the total sum of squares.

import threading


results = [0, 0, 0, 0]


def calculate_sum(start, end, index):

    total = 0

    for i in range(start, end + 1):
        total += i * i

    results[index] = total


t1 = threading.Thread(
    target=calculate_sum,
    args=(1, 25, 0)
)

t2 = threading.Thread(
    target=calculate_sum,
    args=(26, 50, 1)
)

t3 = threading.Thread(
    target=calculate_sum,
    args=(51, 75, 2)
)

t4 = threading.Thread(
    target=calculate_sum,
    args=(76, 100, 3)
)


t1.start()
t2.start()
t3.start()
t4.start()


t1.join()
t2.join()
t3.join()
t4.join()


total_sum = sum(results)

print("Sum calculated by each thread:", results)
print("Total sum of squares:", total_sum)