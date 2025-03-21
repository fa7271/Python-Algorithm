import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

while True:
    dic = defaultdict(int)
    N, M = map(int, input().split())
    if not N and not M:
        break
    for i in range(N):
        for j in map(int, input().split()):
            dic[j] += 1

    scores = sorted(set(dic.values()), reverse=True)
    second = scores[1] if len(scores) > 1 else 0

    for x, y in sorted(dic.items()):
        if y == second:
            print(x, end=" ")
    print()
