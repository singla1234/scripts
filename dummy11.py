from collections import deque



def produce(dq,n):
    for i in range(n):
        dq.appendleft(i)

        if len(dq)==dq.maxlen:
            print("queue full,yield control")
            yield

def consume(dq):
    while True:
        while len(dq)>0:
            print("processing",dq.pop())
        print("queue empty")
        yield

def cordinater():
    dq = deque(maxlen=10)
    pro = produce(dq, 11000)
    con= consume(dq)
    while True:
        try:
            next(pro)
        except StopIteration:
            break
        finally:
            next(con)

cordinater()