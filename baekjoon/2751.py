# input이 클 때
import sys
input = sys.stdin.readline

i = int(input())
numbers = []

for _ in range(i):
    numbers.append(int(input()))

numbers.sort()

for x in range(len(numbers)):
    print(numbers[x])
