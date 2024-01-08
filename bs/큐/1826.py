import heapq
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = sorted([list(map(int, sys.stdin.readline().split(" "))) for _ in range(n)], key=lambda x: x[1])
heaq = []
for i in lst:
    heapq.heappush(heaq, (i[0], -i[1]))
L, P = map(int, sys.stdin.readline().split(" "))
res = []
count = 0
while P < L:
    # 갈 수 있는 곳 찾기
    while heaq and heaq[0][0] <= P:
        next_oil_station, plus_oil = heapq.heappop(heaq)
        heapq.heappush(res, (plus_oil, next_oil_station))

    # 도달 못함
    if not res:
        print(-1)
        exit()

    #     그 중 가장 멀리 가는거 가져오기.
    oil, station = heapq.heappop(res)
    P += - oil
    count += 1
print(count)