circle_count = int(input())


def move(start, target):
    return print(start, target)


def hanoi(circle_count, start, end):
    if circle_count == 0:
        return

    hanoi(circle_count-1, start, 6-start-end)
    move(start, end)
    hanoi(circle_count-1, 6-start-end, end)


print((2**circle_count) - 1)
if circle_count <= 20:
    hanoi(circle_count, 1, 3)


# 하노이 n이랑 시작 타겟기둥
# 발판은 6 - 시작 - 타겟
# 종료조건은  n == 1 일ㅈ때
# return move(1, 3)
#
# hanoi(n-1, start , 발)
# hanoi(1, s, e) or move(s, e)
# hanoi(n-1, 발, e)

# if n<=20
#
