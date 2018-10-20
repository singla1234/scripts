from collections import deque
dq=deque(maxlen=10)
def producer(dq,n):


        for i in range(n):
            dq.append(i)
            print("adding data and value of n is "+str(i))
            if len(dq)==dq.maxlen:
                print("buffer full passing the control to consumer")
                yield

def consumer(dq):
    while True:
        while len(dq)>0:
            dq.pop()
            print("popping the items")
        yield




def cc():
    pro=producer(dq,35)
    con=consumer(dq)
    while True:
        try:
            next(pro)
        except StopIteration:
            break
        finally:
            next(con)

print(cc())