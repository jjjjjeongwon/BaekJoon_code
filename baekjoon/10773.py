import sys
input = sys.stdin.readline

K = int(input())
stack = []

for i in range(K):
    inputNum = input().strip()
    if (inputNum == "0"):
        stack.pop()
    else:
        stack.append(inputNum)
print(sum(map(int, stack)))
