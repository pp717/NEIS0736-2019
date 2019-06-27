import time
import sys
from threading import Thread
from multiprocessing import Process

Rx = 2
Ry = 10**7

def demo1():
    print("demo 1")
    a,b = [],[]
    for i in range(Ry):
        a.append(i*2)
        b.append(i*2)
    print("a[{}] = {}".format(Ry-1,b[Ry-1]))
    print("b[{}] = {}".format(Ry-1,b[Ry-1]))

def demo2():
    a = [i*2 for i in range(Ry)]
    b = [i*2 for i in range(Ry)]
    print("a[{}] = {}".format(Ry-1,b[Ry-1]))
    print("b[{}] = {}".format(Ry-1,b[Ry-1]))

def threaddemo3(tno):
    b = [i*2 for i in range(Ry)]
    print("{}[{}] = {}".format(tno,Ry-1,b[Ry-1]))

def demo3():
    print("demo 3")
    xthreads = []
    for tno in ['a','b']:
        xthread = Thread(target=threaddemo3, args=(tno,))
        xthreads.append(xthread)
        xthread.start()
    for x in xthreads:
        x.join()

def processdemo4(pno):
    b = [i*2 for i in range(Ry)]
    print("{}[{}] = {}".format(pno,Ry-1,b[Ry-1]))

def demo4():
    print("demo 4")
    procs = []
    for pno in ['a','b']:
        proc = Process(target=processdemo4, args=(pno,))
        procs.append(proc)
        proc.start()
    for x in procs:
        x.join()

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
    # -------------------------------------
    start = time.time()
    
    demo4()
    
    end = time.time()
    print("time demo 4 : {}".format(end - start))
    print("-"*45)

# Mem leak