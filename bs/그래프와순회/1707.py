import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**6)
t = int(input())

def dfs(node):
    global result

    # 다음 노드 탐색
    for next_node in graph[node]:
        # 다음 노드 색칠 안 되어 있으면
        if visited[next_node] == -1 :

            # 지금 노드가 1이면 다음 노드는 2이다, 반대도 동일
            if visited[node] == 1:
                visited[next_node] = 2
            elif visited[node] == 2:
                visited[next_node] = 1

            # 그 다음 노드 색칠하러 출발
            dfs(next_node)
        # 다음 노드 이미 방문을 했음
        else:
            #다른 노드가 이미 방문했고, 지금 내가 방문 했는데 색깔이 같으면 안됨
            if visited[node] == visited[next_node]:
                result = False
                return

for _ in range(t):
    v, e = map(int,input().split()) # 정점, 간선
    graph = [[] for _ in range(v+1)]
    # 집합 여부 저장 할 visited
    visited = [-1] * (v+1)
    for _ in range(e):
        a, b = map(int,sys.stdin.readline().split())
        # 양방향 그래프
        graph[a].append(b)
        graph[b].append(a)
        # 이분 그래프 가능여부
    result = True
    # 모든 노드 탐색
    for i in range(1, v+1):
        if visited[i] == -1: # 아직 방문 안 했으면
            visited[i] = 1 # 1 이라는 색으로 색칠
            dfs(i) # 연관 된 다음 노드 칠하러 출발

            # 이분 그래프가 아니면 돌아옴
            if result == False:
                break

    if result == False:
        print("NO")
    # 이분 그래프라면
    else:
        print("YES")