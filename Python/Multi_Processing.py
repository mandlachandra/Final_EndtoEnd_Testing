#Multi Processing means multiple process, each with its own memory space and python interpreter
#Processes are independent and dont share memory
#NO GIL issue because each process runs in a separate interpreter
#Best for CPU -Boun tasks (like heavy calculations)
#
# import multiprocessing
# import time
#
# def print_numbers():
#     for i in range(5):
#         print("thread",i)
#         time.sleep(2)
#
# p1 =multiprocessing.Process(target=print_numbers)
# p2= multiprocessing.Process(target=print_numbers)
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()
# print("Done")