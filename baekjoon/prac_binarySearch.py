arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]


def binarySearch(targetNum, start, end):

    while start < end:
        # start <= end
        midIndex = (start+end)//2
        if arr[midIndex] == targetNum:
            return midIndex
        elif arr[midIndex] < targetNum:
            start = midIndex + 1
        elif arr[midIndex] > targetNum:
            end = midIndex
            # end = midIndex - 1

    return -1


print(binarySearch(3, 0, len(arr) - 1))
