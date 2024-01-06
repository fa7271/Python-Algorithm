import heapq
import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k = map(int, sys.stdin.readline().split(" "))
lst = []

for i in range(n):
    m, v = map(int, sys.stdin.readline().split(" "))
    heapq.heappush(lst, (m, -v))
bags = deque(sorted([int(sys.stdin.readline()) for _ in range(k)]))

res = []
result = 0
# 각 가방에 넣을 수 있는 최대 가치의 보석 담는다.
# 가방은 오름차순으로 작은 가방부터 넣을거 생각한다.

for bag in bags:
    # 가방에 들어 갈 수 있는것들은 다 들어간다
    while lst and bag >= lst[0][0]:
        heapq.heappush(res, heapq.heappop(lst)[1])
    # 그 중에 가장 큰 value값 가진것을 pop해준다.
    # res를 for문 마다 선언을 안 해주는 이유는 어차피 가방에 무게가 작은 수서대로 올라가므로
    # 굳이 안해주고, 다음 높은 밸류를 뽑아주면 된다.
    if res:
        result += - heapq.heappop(res)
    elif not lst:
        break
print(result)

