import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

graph = [deque(list(map(str, sys.stdin.readline().rstrip()))) for _ in range(4)]
t = int(input())


def left(idx, dir):
    # 첫번쨰게 넘어오면 왼쪽은 안돌림
    if idx < 0:
        return
    # 오른쪾꺼랑 다르면
    if graph[idx][2] != graph[idx+1][6]:
        # 돌려주는데 그 왼쪾꺼는 방향이 다름
        left(idx-1 , -dir)
        # 갔다오면 돌려줌
        graph[idx].rotate(dir)
def right(idx, dir):
    # 마지막꺼 안 돌림
    if idx > 3:
        return
    if graph[idx-1][2] != graph[idx][6]:
        right(idx+1, -dir)
        graph[idx].rotate(dir)

# 2 6
for _ in range(t):
    idx, dir = map(int, sys.stdin.readline().rstrip().split())
    # 1부터 시작이라 1 빼줌
    idx -= 1
    # 왼쪽꺼
    left(idx-1, -dir)
    # 오른쪽꺼
    right(idx+1, -dir)
    # 내꺼
    graph[idx].rotate(dir)
res = 0
for i in range(4):
    if graph[i][0] == "1":
        res += 2**i
print(res)
