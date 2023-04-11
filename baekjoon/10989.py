# input이 클 때
import sys
input = sys.stdin.readline

i = int(input())

howManyVisit = list(0 for i in range(10001))

for _ in range(i):
    howManyVisit[int(input())] += 1

for _ in range(len(howManyVisit)):
    if howManyVisit[_] != 0:
        for x in range(howManyVisit[_]):
            print(_)
