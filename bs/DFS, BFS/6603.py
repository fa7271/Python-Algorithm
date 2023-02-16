import sys
from collections import deque


def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(res[i], end=' ')
        print()
        return
    for i in range(start, len(arr)):
        res[depth] = arr[i]
        dfs(i + 1, depth + 1)
res = [0 for i in range(13)]
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    del arr[0]
    dfs(0, 0)
    print()





