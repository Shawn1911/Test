
import threading
import time


def a():
    time.sleep(3)
def b():
    time.sleep(4)

#

# start = time.time()
# a()
# b()
# print(time.time()-start)

#async Myltithread

# start = time.time()
# thread1 = threading.Thread(target= a)
# thread2 = threading.Thread(target= b)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print(time.time()-start)

# start = time.time()
# l = []
# for i in range(1_000_000):
#     thread = threading.Thread(target=a)
#     thread.start()
#     l.append(thread)
#
# for i in l:
#     i.join()
#
# print(time.time()-start)

start = time.time()

print(time.time()-start)