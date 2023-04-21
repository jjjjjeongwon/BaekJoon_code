# import sys
# input = list(map(sys.stdin.readline().split()))

# N = input[0] #건물개수
# C = input[1] #설치공유기 개수

# print(N, C)

# for i in range(N)

n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()  # [1,2,4,8,9]


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2  # 공유기 간 최소거리 찾는 중
        current = array[0]  # 1
        count = 1

        for i in range(1, len(array)):  # 1,2,3,4
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


start = 1  # 집 간 최소거리
end = array[-1] - array[0]  # 집 간 최대거리
answer = 0  # 가장 가까운 공유기 간 거리

binary_search(array, start, end)
print(answer)
