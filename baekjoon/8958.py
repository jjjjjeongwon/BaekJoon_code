a = int(input())

for x in range(a):
    b = list(input())

    count = 0
    sum_count = 0
    for x in b:
        if x == 'O':
            count += 1
            sum_count += count
        else:
            count = 0
    print(sum_count)
