a = int(input())


def isPrime(number):
    if (number < 2):
        return False
    i = 2
    while (i*i <= number):
        if (number % i == 0):
            return False
        i += 1
    return True


for _ in range(a):
    target = int(input())
    for i in range(target//2, 1, -1):
        if (isPrime(i) & isPrime(target-i)):
            print(i, target-i)
            break
