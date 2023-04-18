import sys
input = sys.stdin.readline

N = int(input())
topList = list(map(int, input().split()))

stack = []
# stack에는 [[index, top번호],..]
answerList = [0]*N

for i in range(len(topList)):
    while stack:
        if topList[stack[-1][0]] < topList[i]:
            stack.pop()

        else:
            answerList[i] = stack[-1][0]+1
            break
    stack.append((i, topList[i]))

print(answerList)
