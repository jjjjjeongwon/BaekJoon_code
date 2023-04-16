import sys
input = sys.stdin.readline

T = int(input())
stackList = []


for _ in range(T):
    stack = []
    bracket = input()
    for i in range(int(len(bracket.strip()))):
        if bracket[i] == "(":
            stack.append(1)
        else:
            stack.append(-1)
    stackList.append(sum(stack))

for _ in range(int(len(stackList))):
    if stackList[_] == 0:
        print("YES")
    else:
        print("NO")
