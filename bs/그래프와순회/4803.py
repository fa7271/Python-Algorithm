import heapq, sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]


def union(x, y):
    nx = find(x)
    ny = find(y)

    if nx < ny:
        parent[ny] = nx
    else:
        parent[nx] = ny


case = 0
while True:
    case += 1
    n, m = map(int, sys.stdin.readline().split(" "))
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n + 1)]
    parent = [i for i in range(n + 1)]
    # union-find 함수
    cycle = set()
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split(" "))
        # find (cycle)
        if find(a) == find(b):
            cycle.add(parent[a])
            cycle.add(parent[b])
        # 둘 중 하나라도 사이클에 들어있으면 어차피 사이클임
        if parent[a] in cycle or parent[b] in cycle:
            cycle.add(parent[a])
            cycle.add(parent[b])
        # union
        union(a, b)
    # 경로 압축
    for i in range(n+1):
        find(i)

    parent = set(parent)
    res = len(parent - cycle) - 1
    if res == 0:
        print('Case %d: No trees.' % case)
    elif res == 1:
        print('Case %d: There is one tree.' % case)
    else:
        print('Case %d: A forest of %d trees.' % (case, res))
