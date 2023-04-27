import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

visitedList = []
visited = [False] * (M)

for _ in range(N):
    visitedList.append(visited)


for i in range(1, N+1):
    wood = list(input().strip())
    graph.append(wood)


dxUpDown = [-1, 1]
dyUpDown = [0, 0]

dxLeftRight = [0, 0]
dyLeftRight = [-1, 1]


def DFS(x, y):
    count = 0
    if graph[x][y] == '-':
        visitedList[x][y] = True
        for i in range(2):
            nx = x + dxLeftRight[i]
            ny = y + dyLeftRight[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            print(graph[0][-1])

            if not visitedList[nx][ny] and graph[nx][ny] == '-':
                visitedList[nx][ny] = 1
                print(graph)
                DFS(nx, ny)
        count += 1
        DFS(nx, ny)

    if graph[x][y] == '|':
        visitedList[x][y] = True
        for i in range(2):
            nx = x + dxUpDown[i]
            ny = y + dyUpDown[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if not visitedList[nx][ny] and graph[nx][ny] == '|':
                visitedList[nx][ny] = 1
                DFS(nx, ny)
        count += 1
        DFS(nx, ny)

    return count

    # 가로 다음에는 방문하지 않은 가로 있는지 확인
    # 있으면 방문체크하고 진행
    # 또 있으면 방문체크하고 진행
    # 없으면 count+1하고 상하좌우 중 방문하지 않은 곳에 방문해서 재귀

    # 세로 다음에는 방문하지 않은 세로 있는지 확인
    # 있으면 방문체크하고 진행
    # 없으면 count+1하고 상하좌우 중에 방문하지 않은 곳에 방문해서 재귀


print(DFS(0, 0))
