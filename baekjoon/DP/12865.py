

# dp = [[0 for i in range(K)]for _ in range(N+1)]

# for _ in range(1, N+1):
#     W, V = list(map(int, input().split()))

#     for i in range(K):
#         if i+1 >= W:
#             dp[_][i] = V

# print(dp)

# for i in range(N+1, 1, -1):
#     for j in range(K, 1, -1):
#         # print('체크', max(dp[i-1][j], dp[i][j-1]))
#         print(dp[i][j])

import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))  # 물품의 수, 버틸 수 있는 무게

backpack = []  # 배낭 배열
dp = [0] * (K+1)

for _ in range(1, N+1):
    W, V = list(map(int, input().split()))  # 무게, 가치
    backpack.append([W, V])  # backpack에 무게, 가치 넣음

print(backpack)

for i in backpack:
    weight = i[0]
    value = i[1]
    for j in range(K, weight-1, -1):
        dp[j] = max(dp[j], dp[j-weight]+value)

# print(dp[-1])
