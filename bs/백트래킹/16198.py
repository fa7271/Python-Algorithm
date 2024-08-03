import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
energy = list(map(int, sys.stdin.readline().rstrip().split(" ")))

result = -1e9


def bt(temp):
    global result
    if len(energy) == 2:
        result = max(result, temp)
        return
    for i in range(1, len(energy) - 1):
        E = energy[i - 1] * energy[i + 1]
        pop_num = energy.pop(i)
        bt(temp + E)
        energy.insert(i, pop_num)
bt(0)
print(result)