from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())  # 도시개수, 도로개수, 거리정보, 출발도시번호
graph = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

print(graph)

checkVisitDistanceList = [-1] * (N+1)  # 도시 방문, 거리 담을 배열 생성 -1은 방문 안한것
checkVisitDistanceList[X] = 0  # X번째는 출발도시이므로 방문처리하고 시작

# BFS
queue = deque([X])
print(queue)
while queue:  # queue가 빌때까지
    now = queue.popleft()  # queue의 맨 앞 값을 빼고 now에 저장
    print(now)
    print(queue)
    for i in graph[now]:  # graph의 now번째를 돌면서
        if checkVisitDistanceList[i] == -1:  # 방문하지 않았으면
            # 방문하고 현재거리보다 1을 더해준다
            checkVisitDistanceList[i] = checkVisitDistanceList[now]+1
            queue.append(i)  # queue가 빌때까지 돈다

if K in checkVisitDistanceList:
    for i in range(1, N+1):
        if checkVisitDistanceList[i] == K:
            print(i)
else:
    print(-1)
