def fib():
    a,b=0,1
    while True:
        a,b=a+b,a
        yield a


fb=fib()
for i in range(151):
    print(next(fb))