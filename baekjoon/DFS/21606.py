import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())  # 정점의 개수
# 실내, 외 정보가 담긴 배열/0번 인덱스는 사용하지 않을 거라 [0] 추가해둠
location = [0]+list(map(int, input().strip()))
graph = [[] for _ in range(N+1)]  # 정점 정보 담을 배열 생성
visited = [False] * (N+1)  # 방문 여부 배열 생성


def DFS(V, count):  # count는 실외와 연결된 실내 노드 개수 카운트
    visited[V] = True  # V정점에 대한 방문정보를 True로 바꾼다
    for i in graph[V]:  # V정점에 연결된 정점을 돈다
        if location[i] == 1:  # 연결된 정점이 실내라면
            count += 1  # 실내개수 카운트에 1을 더해줌
        elif not visited[i] and location[i] == 0:
            count = DFS(i, count)
    return count


first_ans = 0
for i in range(N-1):  # graph에 정점 정보 저장
    X, Y = map(int, input().split())
    graph[X].append(Y)
    graph[Y].append(X)

    # X,Y가 인접한 노드인데, 둘 다 실내라면 방문케이스 2가지가 되니까 2개 카운트
    if location[X] == 1 and location[Y] == 1:
        first_ans += 2

second_ans = 0
for i in range(1, N+1):  # for문 돌면서 모든 실외에 대해 second_ans늘려준다
    if not visited[i] and location[i] == 0:  # 방문안했으면서 && 실외라면 => DFS 재귀
        x = DFS(i, 0)  # 방문안했으면서 실외인 i에 대해서 진행/ count는 초기이기 때문에, 0
        second_ans += x * (x-1)  # 실외노드 기준 인접노드 세기 => n *(n-1)

print(first_ans+second_ans)
