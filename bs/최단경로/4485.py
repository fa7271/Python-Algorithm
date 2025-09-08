import heapq
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
idx = 1
while True:
    x = int(input())
    if x == 0:
        break
    graph = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(x)]
    heap = []
    heapq.heappush(heap, (graph[0][0], 0, 0))
    dist = [[1e9] * x for _ in range(x)]
    dist[0][0] = graph[0][0]
    while heap:
        cur_w, cur_node_x, cur_node_y = heapq.heappop(heap)
        for dx, dy in move:
            next_node_x = dx + cur_node_x
            next_node_y = dy + cur_node_y
            if 0 <= next_node_x < x and 0 <= next_node_y < x:
                d = cur_w + graph[next_node_x][next_node_y]
                if d < dist[next_node_x][next_node_y]:
                    dist[next_node_x][next_node_y] = d
                    heapq.heappush(heap, (dist[next_node_x][next_node_y], next_node_x, next_node_y))
    print(f"Problem {idx}: {dist[-1][-1]}")
    idx += 1
