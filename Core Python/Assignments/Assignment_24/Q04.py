# 4. Implement a producer-consumer problem with a limited buffer of size 5. Create two
# producer threads and two consumer threads. Producers produce items, and consumers
# consume them. Ensure proper synchronization to avoid buffer overflows or underflows.


import threading
import time
import random


buffer = []
BUFFER_SIZE = 5

condition = threading.Condition()


def producer(producer_id):

    for i in range(5):

        item = f"Item-{producer_id}-{i}"

        with condition:

            while len(buffer) == BUFFER_SIZE:
                print(f"Producer {producer_id}: Buffer is full, waiting...")
                condition.wait()

            buffer.append(item)

            print(f"Producer {producer_id} produced: {item}")
            print("Buffer:", buffer)

            condition.notify_all()

        time.sleep(random.uniform(0.5, 1.5))


def consumer(consumer_id):

    for i in range(5):

        with condition:

            while len(buffer) == 0:
                print(f"Consumer {consumer_id}: Buffer is empty, waiting...")
                condition.wait()

            item = buffer.pop(0)

            print(f"Consumer {consumer_id} consumed: {item}")
            print("Buffer:", buffer)

            condition.notify_all()

        time.sleep(random.uniform(0.5, 1.5))


p1 = threading.Thread(target=producer, args=(1,))
p2 = threading.Thread(target=producer, args=(2,))

c1 = threading.Thread(target=consumer, args=(1,))
c2 = threading.Thread(target=consumer, args=(2,))


p1.start()
p2.start()
c1.start()
c2.start()


p1.join()
p2.join()
c1.join()
c2.join()


print("\nAll producers and consumers have finished.")