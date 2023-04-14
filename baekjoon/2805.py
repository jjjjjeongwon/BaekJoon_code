import sys
input = sys.stdin.readline

N, M = map(int, input().split())

tree_height = list(map(int, input().split()))
start = 1
end = max(tree_height)

while start <= end:
    count = 0
    mid = (start+end)//2
    for i in tree_height:
        if i > mid:
            count += i - mid
    if count >= M:
        start = mid + 1
    else:
        end = mid-1

print(end)
