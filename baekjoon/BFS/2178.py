from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = list(list(map(int, sys.stdin.readline().strip())) for _ in range(N))


def BFS(x, y):
    # 네가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()  # 큐 선언
    queue.append((x, y))  # 큐에 탐색하고자 하는 위치를 넣는다

    while queue:  # queue가 비기 전까지
        x, y = queue.popleft()  # queue의 첫번째 값을 pop하고 각각 x, y에 저장

        for i in range(4):  # 4가지 방향으로 위치확인
            nx = x + dx[i]  # pop한 queue의 첫번째 x값에 0-3으로 상하좌우 확인
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:  # nx는 세로줄 개수 ny는 가로줄 개수
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]


print(BFS(0, 0))
