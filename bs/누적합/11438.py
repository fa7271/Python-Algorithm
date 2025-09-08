import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
LENGTH = 21

n = int(input())
parent = [[0] * LENGTH for _ in range(n + 1)]
visited = [False] * (n + 1)
d = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x, depth):
    visited[x] = True
    d[x] = depth

    for node in graph[x]:
        if visited[node]:
            continue
        # 바로 한 단계 위에 부모
        parent[node][0] = x
        dfs(node, depth + 1)

def set_parent():
    # 한 단계 부모 갱신
    dfs(1, 0)
    for i in range(1, LENGTH):
        for j in range(1, n + 1):
            # 각 노드에 대해 2**i번째 부모 정보 갱신
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

# j 노드의 2**i 번째 노드를 저장한다.
# parent[j][i] = parent[parent[j][i - 1]][i - 1]
# j 노드의 2**i 번째 조상을 저장한다.
# parent[i][j] = parent[parent[i][parent[i-1][j]]]

def lca(a, b):
    # 무조건 b의 깊이가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # a와 b의 깊이가 동일해주도록 설정
    for i in range(LENGTH - 1, -1, -1):
        if d[b] - d[a] >= 2**i:
            b = parent[b][i]

    if a == b:
        return a

    # 올라가면서 공통 조상 찾기
    for i in range(LENGTH - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


set_parent()
print(parent[15])
m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
