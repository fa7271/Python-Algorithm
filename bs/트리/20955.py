import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().split(" "))
graph = [[] for _ in range(n + 1)]
parents = [i for i in range(n + 1)]

count = 0
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    X = find(x)
    Y = find(y)
    # 사이클을 형성하지 않은경우
    if X < Y :
        parents[Y] = X
    else:
        parents[X] = Y
for r in range(m):
    x, y = map(int, sys.stdin.readline().split(" "))
    # 부모가 다른경우 관계를 끊어 줘야함
    if find(x) == find(y):
        count += 1
    union(x, y)

# 다르면 연결 해줘야함
link = 0
sets = set()
for i in range(1,n+1):
    sets.add(find(i))
print(len(sets)-1 + count)

