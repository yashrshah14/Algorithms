def fibonacci(n):
    if n<1:
        return
    f1=0
    f2=1
    for i in range(n):
        print f1,
        next=f1+f2
        f1=f2
        f2=next

fibonacci(9)