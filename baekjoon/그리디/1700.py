N, K = map(int, input().split())

orders = list(map(int, input().split()))  # [2,3,2,3,1,2,7]

plugList = [0]*(N)  # 플러그 배열 만들기 [0,0]
count = 0

for i in range(K):  # 사용순서 리스트 길이만큼 돈다
    if orders[i] in plugList:  # 사용순서 리스트에 인덱스에 해당하는 숫자 있으면 for문 다시 돌기 없으면 elif로
        continue
    elif 0 in plugList:  # 리스트에 0이 있으면 밑에줄 실행
        # 플러그리스트 0이 있는 인덱스에 orders[i] 넣음
        plugList[plugList.index(0)] = orders[i]
        continue  # 다시 for문 진행
    count += 1  # 둘 다 false면 count 1개 더해줌
    pop_index = i
    supply_index = 0
    for j in range(N):  # 플러그 리스트 길이만큼
        if plugList[j] in orders[i+1:]:  # 플러그리스트 숫자가 orders 넣은거 뒤부터 만든 배열에 있으면
            tem_index = orders.index(plugList[j], i)
            if tem_index > pop_index:
                pop_index = tem_index
                supply_index = j
        else:
            supply_index = j
            break
    plugList[supply_index] = orders[i]

print(count)
