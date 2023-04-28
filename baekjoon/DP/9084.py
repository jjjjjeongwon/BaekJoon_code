import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):  # 테스트케이스 개수만큼
    N = int(input())  # 동전개수
    coins = list(map(int, input().split()))  # 동전 종류
    M = int(input())  # 금액

    priceList = [0] * (M+1)
    priceList[0] = 1

    for coin in coins:  # 동전 종류만큼 돈다
        for i in range(M+1):  # 금액만큼 돈다
            # 금액이 동전 보다 크면 (ex. i가 5원, coin이 7원이면/7원으로 5원 만들수 없기 때문에 처리할 필요 없음)
            if i >= coin:
                priceList[i] += priceList[i - coin]

    print(priceList[M])
