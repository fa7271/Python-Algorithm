import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int,input().split())

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(left, right):
    left = find(left)
    right = find(right)
    if left < right:
        parent[right] = left
    else:
        parent[left] = right
parent = [i for i in range(n+1)]

count = 0
for _ in range(m):
    a,b = map(int,input().split())
    if find(a) != find(b):
        union(a,b)
        count += 1
        if count == n-2 :
            print(0,0)
            exit()
board = [list(map(int, input().split())) for _ in range(n)]
edges = []
# 1번은 모든 컴퓨터와 연결 되어 있으므로 패스, 양방향이므로 체크 해줌
for i in range(1, n - 1):
    for j in range(i + 1, n):
        edges.append((i + 1, j + 1, board[i][j]))

edges.sort(key = lambda x:x[2])
mst = 0 # 비용
connect_mst = [] # 연결한 mst
for u, v, e in edges:
    # 부모가 다르면 연결이 안된 상태
    if find(u) != find(v):
        union(u,v)
        count += 1
        mst += e
        connect_mst.append((u,v))
        if count == n - 2: # 안정적인 네트워크가 되었다면
            print(mst, len(connect_mst)) # 답 출력 후, 중지
            for u, v in connect_mst:
                print(u, v)
            exit()
