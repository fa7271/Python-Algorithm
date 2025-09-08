import sys, heapq
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, e = map(int,sys.stdin.readline().split())
graph =[[] for _ in range(n+1)]
# 양방향 간선

def find(start, end):
    dist = [float("inf")] * (n+1)
    dist[start] = 0
    hq = [(0,start)]
    while hq:
        cur_w, cur_node = heapq.heappop(hq)
        # 현재 가중치 값보다 다음노드 값이 크면 굳이 방문 안 해도 됨
        if cur_w > dist[cur_node]:
            continue
        for to_node, to_w in graph[cur_node]:
            d = dist[cur_node] + to_w
            if d < dist[to_node]:
                dist[to_node] = d
                heapq.heappush(hq,(d,to_node))
    return dist[end]

for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int,sys.stdin.readline().split())
res1 = find(1, v1) + find(v1,v2) + find(v2,n)
res2 = find(1,v2) + find(v2,v1) + find(v1,n)
if res1 == float("INF") and res2 == float("INF"):
    print(-1)
else:
    print(min(res1,res2))

# 세준이는 1번 정점에서 N번까지 , v1,v2 필수

