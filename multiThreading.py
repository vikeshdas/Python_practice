
"""
- In python at a time only one thread can be run because python use GIL(Global intepreter lock) which allow only one thread to excute at a time.

- If we have CPU Intesive task in that case we should create multiprocessing. In multiprocessing one processing will use whose processor for all time.

- If we have I/O intensive task in that case we shoud create single processing and inside that single processing create multiple thread.Since it is I/O intesive cpu will be definatly ideal for some time ,when cpu is ideal other thread will be excuted.

- what is benifits of GIL?
"""


# multiprocessing exmaple

import multiprocessing as mp
# import time


# def name_and_time(name):
#     print(f'Hello {name}, currect time is {time.time()}')
#     print("Sleeping for 2 second")
#     time.sleep(2)
#     print("after sleep exiting function")


# if __name__=="__main__":
#     process_list=list()
#     for i in range(5):
#         process=mp.Process(target=name_and_time,args=("Vikesh",))
#         process_list.append(process)
    
#     for p in process_list:
#         p.start()
    
#     print("other instruction of the main module...")
#     print("end of script")


# multithreading exmaple
# import threading
# import time

# def name_and_time(name):
#     print(f'Hello {name}, current time is {time.time()}')
#     print('Sleeping for 2 seconds ...')
#     time.sleep(2)
#     print('After sleeping ... exiting function.')
 

# if __name__ == '__main__':
#     thread_list = list()     
#     for i in range(10):
#         thread = threading.Thread(target=name_and_time, args=('Andrei',))
#         thread_list.append(thread) 

#     for t in thread_list:
#         t.start()


"""
- This counter is defined in the main process.

-That child process gets its own separate copy of the memory space.

-So global counter inside increment() refers to the child's copy, not the main one.

-Any change made inside the child process is not reflected back in the main process.

SO below program will not excute becauese in child process there is no counter define so it woul give error.
"""
# def increment():
#     global counter
#     counter+=1

# if __name__=='__main__':
#     counter=1

#     for i in range(10):
#         process=mp.Process(target=increment,args=())
#         process.start()
#         process.join()

#     print(counter)


"""
In above program we ar basically tring to share counter variable between two process child processs and main process 

Below is solution to share data between two process
"""

# def increment(counter):
#     counter.value+=1

# if __name__=='__main__':
#     # i means integer and 1 is initialization
#     counter = mp.Value('i', 1)

#     for i in range(10):
#         process=mp.Process(target=increment,args=(counter,))
#         process.start()
#         process.join()

#     print(counter)


"""
Example where we face problem without lock in variable.

"""
import multiprocessing as mp
import time
 
def deposit(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value += 1
 
def withdraw(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value -= 1
 
if __name__ == '__main__':
    balance = mp.Value('i', 500)   
    print(f'Balance BEFORE running processes: {balance.value}')
 
    p1 = mp.Process(target=deposit, args=(balance,))
    p2 = mp.Process(target=withdraw, args=(balance,))
 
    p1.start()
    p2.start()
 
    p1.join()
    p2.join()
 
    print(f'Balance AFTER running processes: {balance.value}')