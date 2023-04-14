import sys
input = sys.stdin.readline

N_count = int(input())

N_arr = list(map(int, input().split()))

N_arr.sort()  # arr 정렬 완료

target_count = int(input())

target_arr = list(map(int, input().split()))


def binarySearch(target, start, end):
    while start < end:  # start가 end보다 작을때만
        # (기존) start <= end
        midIndex = (start+end)//2
        if N_arr[midIndex] == target:
            return 1
        elif N_arr[midIndex] > target:
            end = midIndex
            # (기존) end = midIndex +1
        elif N_arr[midIndex] < target:
            start = midIndex + 1
    if N_arr[start] == target:
        return 1
    return 0


for _ in range(target_count):
    print(binarySearch(target_arr[_], 0, len(N_arr)-1))
