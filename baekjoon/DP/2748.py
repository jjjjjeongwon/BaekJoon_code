import sys

input = sys.stdin.readline
n = int(input())

fib = [-1]*(n+1)


def fibo(num):
    if num == 0:
        fib[0] = 0
        return 0
    if num == 1:
        fib[1] = 1
        return 1

    if fib[num] != -1:
        return fib[num]
    else:
        fib[num] = fibo(num-1)+fibo(num-2)
        return fib[num]


fibo(n)

print(fib[n])


#####################
