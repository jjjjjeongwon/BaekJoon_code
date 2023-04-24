import sys
input = sys.stdin.readline

V, E = map(int, input().split())

parent = [0] * (V+1)  # node의 개수만큼 [0,0,0,..] parent 배열로 초기화
for i in range(1, V+1):
    parent[i] = i


def find_parent(parent, x):
    # parent배열의 x번째가 자기자신과 다른 경우/부모노드가 자기자신이 아닌경우(초기값말고 바뀐 경우)
    if parent[x] != x:
        # parent배열의 x번째값을 find_parent()함수로 부모를 찾아서 변경
        parent[x] = find_parent(parent, parent[x])
    return parent[x]  # 찾은 부모 리턴


def union_parent(parent, a, b):
    a = find_parent(parent, a)  # a는 find_parent로 찾은 a의 부모
    b = find_parent(parent, b)
    if a < b:  # a가 b보다 작으면, b의 부모를 a로 바꿈
        parent[b] = a
    else:  # b가 a보다 작으면, a의 부모를 b로 바꿈
        parent[a] = b


edges = []
total_cost = 0

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()  # 간선정보 기준 오름차순 정렬

for i in range(E):
    cost, a, b = edges[i]

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)
