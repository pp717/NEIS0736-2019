import time
from threading import Thread

Rx = 2
Ry = 10**7
bt = [[],[]]

def demo1():
    print("demo 1")
    b = [[],[]]
    for i in range(Rx):
        for j in range(Ry):
            b[i].append(i+j*2)
    print("b[{}][{}] = {}".format(Rx-1,Ry-1,b[Rx-1][Ry-1]))

def demo2():
    print("demo 2")
    b = [[i+j*2 for j in range(Ry)] for i in range(Rx)]
    print("b[{}][{}] = {}".format(Rx-1,Ry-1,b[Rx-1][Ry-1]))

def threaddemo3(i):
    bt[i] = [i+j*2 for j in range(Ry)] # for i in range(Rx)]

def demo3():
    print("demo 3")
    xthreads = []
    for thno in range(Rx):
        xthread = Thread(target=threaddemo3, args=(thno,))
        xthreads.append(xthread)
        xthread.start()
    for x in xthreads:
        x.join()
    print("bt[{}][{}] = {}".format(Rx-1,Ry-1,bt[Rx-1][Ry-1]))

if __name__ == '__main__':
    print("Time Measuring in Python")
    print("-"*45)
    # -------------------------------------   
    start = time.time()
    
    demo1()
    
    end = time.time()
    print("time demo 1 : {}".format(end - start))
    print("-"*45)
    # -------------------------------------
    start = time.time()
    
    demo2()
    
    end = time.time()
    print("time demo 2 : {}".format(end - start))
    print("-"*45)
    # -------------------------------------
    start = time.time()
    
    demo3()
    
    end = time.time()
    print("time demo 3 : {}".format(end - start))
    print("-"*45)


