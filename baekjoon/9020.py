# a = int(input())


# def isPrime(number):
#     if (number < 2):
#         return False
#     i = 2
#     while (i*i <= number):
#         if (number % i == 0):
#             return False
#         i += 1
#     return True


# for _ in range(a):
#     target = int(input())
#     for i in range(target//2, 1, -1):
#         if (isPrime(i) & isPrime(target-i)):
#             print(i, target-i)
#             break


import sys
input = sys.stdin.readline

# 소수판별함수


def isPrime(num):
    if num < 2:
        return False
    i = 2
    while (i*i <= num):
        if num % i == 0:
            return False
        i += 1
    return True


# print('ss', isPrime(9))

# def findGold(num):

#     for _ in range(num):
#         a = sys.stdin.readline().strip()
#         print(a)


#     return True
# print(findGold(input))

for _ in range(int(input())):

    a = int(input())
    print(isPrime(a//2))
    for i in range(a//2, 1, -1):
        if isPrime(i) and isPrime(a-i):
            print(i, a-i)
            break
