import sys
from collections import deque, defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

l, n, k = map(int, sys.stdin.readline().rstrip().split(" "))

arr = list(map(int, input().split(" ")))
Q = deque()
light = defaultdict()
move = (-1, 1)
for i in arr:
    Q.append(i)
    light[i] = 0
count = 0
while Q:
    node = Q.popleft()
    count += 1
    for dx in move:
        next_node = dx + node
        if 0 <= next_node <= l and next_node not in light:
            light[next_node] = light[node] + 1
            Q.append(next_node)
    if count == k:
        break
light = sorted(light.items(), key=lambda x: x[1])
for i in range(k):
    print(light[i][1])
