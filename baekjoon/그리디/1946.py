import sys
input = sys.stdin.readline

T = int(input())


for i in range(T):
    N = int(input())
    count = 1
    scoreList = []
    for i in range(N):
        A, B = list(map(int, input().split()))
        scoreList.append([A, B])

    a = scoreList.sort()

    print(a)
