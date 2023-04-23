import sys
sys.setrecursionlimit(10**6)
num_list = []
input = sys.stdin.readline

while True:
    try:
        num = int(input())
        num_list.append(num)  # num_list 생성
    except:
        break


def postorder(first, end):
    if first > end:  # 첫 턴 : 0 > 8
        return
    mid = end+1
    for i in range(first+1, end+1):  # for i in range(1, 9):
        if num_list[first] < num_list[i]:  # num_list[0] < num_list[1,2,3,4,....9]일때
            mid = i  # mid = i로 바꾼다 (가운데 값 설정) 처음값은 6
            break

    postorder(first+1, mid-1)  # postorder(1, 5?) left만하고
    postorder(mid, end)  # right만 처리
    print(num_list[first])  # 여기는 뭔데 다시 보기 이줄만;;;


postorder(0, len(num_list)-1)  # first==0, end==num_list의 길이 -1 ==8
