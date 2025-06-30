import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = list(map(int, input().rstrip().split()))
graph = [[] for _ in range(v + 1)]
parent = [i for i in range(v + 1)]
for _ in range(e):
    a, b = list(map(int, input().rstrip().split()))
    if find(a) != find(b):
        union(a, b)
    graph[a].append(b)
    graph[b].append(a)

temp = find(parent[1])
if not all(find(el) == temp for el in parent[1:]): # 연결되지 않은 경우
    print('NO')
    exit()
홀짝 = [len(i) % 2 for i in graph[1::]]

if all(i == 0 for i in 홀짝) or 홀짝.count(1) == 2:
    print("YES")
else:
    print("NO")
exit()