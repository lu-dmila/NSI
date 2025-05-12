import threading
lA=threading.Lock()
lB=threading.Lock()
lC=threading.Lock
def p1():
    lA.acquire()
    print("LED PRIMAIRE")
    lB.acquire()
    print("LED SECONDAIRE")
    lB.release()
    lA.release()

def p2():
    lB.acquire()
    print("LED PRIMAIRE")
    lC.acquire()
    print("LED SECONDAIRE")
    lB.release()
    lC.release()
    
def p3():
    lC.acquire()
    print("LED PRIMAIRE")
    lA.acquire()
    print("LED SECONDAIRE")
    lA.release()
    lC.release()

t1 = threading.Thread(target=p1, args=[])
t2 = threading.Thread(target=p2, args=[])
t3 = threading.Thread(target=p3, args=[])
t1.start()
t2.start()
t3.start()


