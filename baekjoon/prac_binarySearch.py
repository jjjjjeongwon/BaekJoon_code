arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]


def binarySearch(arr, targetNum):
    start = 0
    end = len(arr) - 1

    while start <= end:
        midIndex = (start+end)//2
        if arr[midIndex] == targetNum:
            return midIndex
        elif arr[midIndex] < targetNum:
            start = midIndex + 1
        elif arr[midIndex] > targetNum:
            end = midIndex - 1

    return -1


print(binarySearch(arr, 3))
