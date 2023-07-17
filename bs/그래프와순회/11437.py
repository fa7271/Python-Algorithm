
import sys
sys.setrecursionlimit(100000)
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(sys.stdin.readline()) # 16
graph = [[] for _ in range(N+1)]


# 양방향 노드 설정
for i in range(N-1):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[x].append(y)
    graph[y].append(x)

parent = [0] * (N + 1)      # 각 노드의 부모 노드 정보
depth = [0] * (N + 1)       # 각 노드까지의 깊이
visited = [0] * (N + 1)     # 방문 여부
def dfs(x, idx):
    visited[x] = 1 # 방문처리해주고
    depth[x] = idx # 방문했으니 현재위치의 depth를 idx로 해줌 기본은 0
    for node in graph[x]: # 그 다음 방문위치
        if visited[node] == 1: # 이미 방문했으면
            continue # 넘어가고
        parent[node] = x # 그렇지 않으면 자식들이니깐 자식들의 부모는 내가 됨
        dfs(node, idx + 1) # 깊이탐색출발 깊이는 1 늘림
dfs(1,0)

def find_parent(left, right):

    # 깊이를 맞춰줌
    while depth[left] != depth[right]: # 깊이가 다르다.
        if depth[left] > depth[right]: # 왼쪽이 더 깊으면
            left = parent[left] # 깊이가 맞을때까지 부모로 올라옴
        else:
            right = parent[right] # 반대도 동일
    # 노드 맞추기
    while left != right: # 노드가 다르면
        left = parent[left] # 노드의 부모로 올라옴
        right = parent[right] # 노드의 부모로 올라옴
    # 주의할점 4의 조상이 2 일때 2와 4 의 공통부모는 2이다. 2는 자기자신이 부모인것이다.

    return left # 맞으면 리턴

# 문제 출력
m = int(sys.stdin.readline())

for i in range(m):
    left, right = map(int,sys.stdin.readline().split(" "))
    print(find_parent(left,right))
