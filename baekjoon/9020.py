a = input()

ans_cnt = 0

if int(a) <= 99:
    ans_cnt = int(a)
elif int(a) == 1000:
    ans_cnt = 144
else:
    ans_cnt += 99
    for _ in range(100, int(a)+1):
        num_list = list(map(int, str(_)))
        if num_list[0]-num_list[1] == num_list[1] - num_list[2]:
            ans_cnt += 1

print(ans_cnt)
