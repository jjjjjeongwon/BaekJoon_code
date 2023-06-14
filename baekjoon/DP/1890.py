import sys
input = sys.stdin.readline

N = int(input())

routeList = []
dp = [[0 for i in range(N)] for _ in range(N)]
count = 2

for i in range(N):
    routeList.append(list(map(int, input().split())))
print(routeList)

# dfs...?
# dp테이블을 어떤 규칙으로 생성할지 더 고민해보기
dp[routeList[0][0]][0] = 1
dp[0][routeList[0][0]] = 1
print(dp)
print(dp[routeList[0][0]][0], dp[0][routeList[0][0]])
