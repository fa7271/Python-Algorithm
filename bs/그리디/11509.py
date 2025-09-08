import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = list(map(int, sys.stdin.readline().split(" ")))
res = [0] * (n + 1)
for x in lst:
    # 화살이 있음
    if res[x] > 0:
        # 그 다음 화살 높이로 간다.
        res[x] -= 1
        res[x - 1] += 1

    else:
        res[x - 1] += 1

print(sum(res))
