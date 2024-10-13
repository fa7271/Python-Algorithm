import sys

sys.setrecursionlimit(100000)
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


def dfs(node):
    # node 가 할 수 있는일들
    for next_node in graph[node]:
        if not check[next_node]:
            check[next_node] = True
            # 아직 두지 않았거나, 거기 있는 사람이 다른일을 할 수 있음.
            if visited[next_node] == -1 or dfs(visited[next_node]):
                visited[next_node] = node
                return True
    return False
    # 축사 배정


n, m = map(int, sys.stdin.readline().rstrip().split())

# 축사
visited = [-1] * (m + 1)

graph = [list(map(int, sys.stdin.readline().rstrip().split()[1::])) for _ in range(n)]

# n번째 소, m개의 가능 숙소
result = 0

for i in range(n):
    # 둘 수 있으면
    check = [False] * (m + 1)
    if dfs(i):
        # 결과 증가
        result += 1
print(result)
