import heapq
import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

T = int(input())
for _ in range(T):
    min_heap = []
    max_heap = []
    k = int(input())
    visited = [1] * k

    for i in range(k):
        order, num = input().split()
        num = int(num)
        if order == "I":
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
        else:
            ## 원소를 제거함과 동시에 해당하는 숫자의 인덱스를 통해 visited의 1을 0으로 삭제되었음을 표시.
            if num == -1:
                if min_heap:
                    visited[heapq.heappop(min_heap)[1]] = 0
            elif num == 1:
                if max_heap:
                    visited[heapq.heappop(max_heap)[1]] = 0
        ## 다음 제거 대상이 될 인덱스에 있는 원소가 이미 다른 쪽에서 지워진 원소면 제거
        while min_heap and visited[min_heap[0][1]] == 0:
            heapq.heappop(min_heap)
        while max_heap and visited[max_heap[0][1]] == 0:
            heapq.heappop(max_heap)

    if min_heap == []:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])