import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**6)

N, M = map(int,sys.stdin.readline().split(" "))
parents = [i for i in range(N+1)] # 부모는 자기자신

def find(x):
    if parents[x] != x:
        parents[x] =  find(parents[x])
    return parents[x]
def union(x,y): # 작은 수로 합 해주면 됨.
    xx = find(x)
    yy = find(y)
    if xx > yy:
        parents[xx] = yy
    else:
        parents[yy] = xx


for i in range(M):
    status, V, E = map(int,sys.stdin.readline().split(" "))
    if status == 0:
        union(V,E)
    else:
        if find(V) == find(E):
            print("YES")
        else:
            print("NO")