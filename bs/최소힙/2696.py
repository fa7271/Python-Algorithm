import sys
import heapq

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(input())

for _ in range(t):
    m = int(input())
    arr = []
    for _ in range(m // 10 + 1):
        arr += list(map(int, input().split()))
    left, right, res = [], [], [arr[0]]
    mid = arr[0]
    for idx, num in enumerate(arr[1:], start=1):
        if num >= mid:
            heapq.heappush(right, num)
        else:
            heapq.heappush(left, -num)
        if idx % 2 == 0:
            if len(left) > len(right):
                heapq.heappush(right, mid)
                mid = -heapq.heappop(left)
            elif len(left) < len(right):
                heapq.heappush(left, -mid)
                mid = heapq.heappop(right)
            res.append(mid)
    print(len(left) +1)
    print(*res)
