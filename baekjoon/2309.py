import sys

dwarf = list(int(sys.stdin.readline()) for _ in range(9))


for i in range(0, 8):
    for j in range(i+1, 9):
        if sum(dwarf) - dwarf[i] - dwarf[j] == 100:
            dwarf = dwarf[:j] + dwarf[j+1:]
            dwarf = dwarf[:i] + dwarf[i+1:]
            dwarf.sort()
            print(*dwarf, sep="\n")
            exit()
