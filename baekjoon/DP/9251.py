import sys
input = sys.stdin.readline

firstStr = list(input().strip())
secondStr = list(input().strip())


# dp = [0 for _ in range(len(secondStr)+1)]
# dpList = [dp for _ in range(len(firstStr)+1)]
dpList = list(list(0 for _ in range(len(secondStr) + 1))
              for _ in range(len(firstStr) + 1))

# print(dpList)

# print(firstStr)

for i in range(1, len(firstStr)+1):
    for j in range(1, len(secondStr)+1):
        if firstStr[i-1] == secondStr[j-1]:
            dpList[i][j] = dpList[i-1][j-1] + 1
        elif firstStr[i-1] != secondStr[j-1]:
            dpList[i][j] = max(dpList[i][j-1], dpList[i-1][j])

print(dpList[-1][-1])
