# n = int(input())
# arr = list(map(int, input().split(' ')))
# arr.sort()

# left = 0
# right = n-1

# answer = abs(arr[left] + arr[right])
# final = [arr[left], arr[right]]


# while left < right:
#     left_val = arr[left]
#     right_val = arr[right]

#     sum = left_val + right_val

#     if abs(sum) < answer:
#         answer = abs(sum)
#         final = [left_val, right_val]
#         if answer == 0:
#             break
#     if sum < 0:
#         left += 1
#     else:
#         right -= 1

# print(final[0], final[1])


import sys
input = sys.stdin.readline

N = int(input())

solutionList = sorted(list(map(int, input().split())))


left = 0
right = N-1
final = [solutionList[left], solutionList[right]]

answer = abs(solutionList[left]+solutionList[right])

while left < right:
    left_val = solutionList[left]
    right_val = solutionList[right]

    sum = left_val+right_val

    if abs(sum) < answer:
        answer = abs(sum)
        final = [left_val, right_val]

        if answer == 0:
            break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])
