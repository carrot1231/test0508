def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)
a=int(input("你想知道第N个数："))
print("第N个数为：",fib(a))
