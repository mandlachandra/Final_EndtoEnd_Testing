#Multi Threading means running multiple threads within in a single process
#Each thread share the same memory space for the process
#Threads are light weight
#Useful for I/O- bound tasks

import threading
import time

def print_numbers():
    for i in range(5):
        print("Thread:",i)
        time.sleep(2)

#create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_numbers)

t1.start()
t2.start()

t1.join()
t2.join()
print("Done!")