import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))  # 숫자 리스트
# 연산자 리스트( +, -, *, /)순으로 개수까지 들어있음
operatorList = list(map(int, input().split()))

maxValue = -0x7fffffff
minValue = 1000000009

#
#   idx 번째의 숫자까지 도달했을떄
#   연산결과가 result 이다.
#   남은 연산자가 있으면, 그 연산자들에 대해 진행한다.
#


def DFS(result, idx):
    global maxValue, minValue

    if idx == N-1:  # 마지막은 이렇게 처리한다
        maxValue = max(maxValue, result)
        minValue = min(minValue, result)
        return
    if operatorList[0] != 0:  # +가 있으면
        num = result+numList[idx+1]  # 두개를 더함(결과와 그 다음 숫자)
        operatorList[0] = operatorList[0]-1
        DFS(num, idx+1)
        operatorList[0] = operatorList[0]+1
    if operatorList[1] != 0:  # -가 있으면
        num = result-numList[idx+1]  # 두개를 뺀다
        operatorList[1] = operatorList[1]-1
        DFS(num, idx+1)
        operatorList[1] = operatorList[1]+1
    if operatorList[2] != 0:  # *가 있으면
        num = result*numList[idx+1]  # 두개를 곱함
        operatorList[2] = operatorList[2]-1
        DFS(num, idx+1)
        operatorList[2] = operatorList[2]+1
    if operatorList[3] != 0:  # //가 있으면
        if result < 0:
            num = (-result)//numList[idx+1] * (-1)  # 두개를 나눔
        else:
            num = result//numList[idx+1]
        operatorList[3] = operatorList[3]-1
        DFS(num, idx+1)
        operatorList[3] = operatorList[3]+1


DFS(numList[0], 0)

print(maxValue)
print(minValue)
