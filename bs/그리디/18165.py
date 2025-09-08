import heapq
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split())) + [0, 0]

rst = 0
for i in range(len(arr) - 2):

    if arr[i + 1] > arr[i + 2]:
        buy = min(arr[i], arr[i + 1] - arr[i + 2])

        rst += 5 * buy
        arr[i] -= buy
        arr[i + 1] -= buy

        # 7원 주고삼
        buy = min(arr[i], arr[i + 1], arr[i + 2])

        rst += 7 * buy

        arr[i] -= buy
        arr[i + 1] -= buy
        arr[i + 2] -= buy

        # 나머지 3원
        rst += 3 * arr[i]
        arr[i] = 0
    else:

        buy = min(arr[i], arr[i + 1], arr[i + 2])

        rst += 7 * buy
        arr[i] -= buy
        arr[i + 1] -= buy
        arr[i + 2] -= buy

        buy = min(arr[i], arr[i + 1])

        rst += 5 * buy
        arr[i] -= buy
        arr[i + 1] -= buy

        rst += 3 * arr[i]
print(rst)
