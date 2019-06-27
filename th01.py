import time
Rx = 10**7

def demo1():
    start = time.time()

    print("demo 1")
    a = range(Rx)
    b = []
    for i in a:
        b.append(i*2)
    print("b[{}] = {}".format(Rx-1,b[Rx-1]))

    end = time.time()
    print("time demo 1 : {}".format(end - start))

def demo2():
    start = time.time()

    print("demo 2")
    a = range(Rx)
    b = [i*2 for i in a]
    print("b[{}] = {}".format(Rx-1,b[Rx-1]))

    end = time.time()
    print("time demo 2 : {}".format(end - start))

if __name__ == '__main__':
    print("Time Measuring in Python")
    demo1()
    print("-"*45)
    demo2()
    print("-"*45)



