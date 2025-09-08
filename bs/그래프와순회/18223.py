import heapq
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

V, E, P= map(int,sys.stdin.readline().split(" "))
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v, w))
    graph[v].append((u,w))

def solution(start, end):
    dist = [float('inf')]*(V+1)
    hq = [(0,start)]
    while hq:
        cur_w, cur_node = heapq.heappop(hq)
        if cur_node == end:
            return cur_w
        for to_node, to_w in graph[cur_node]:
            d = cur_w + to_w

            if d < dist[to_node]:
                dist[to_node] = d
                heapq.heappush(hq,(d,to_node))
if solution(1,V) == (solution(1,P) + solution(P,V)):
    print("SAVE HIM")
else:
    print("GOOD BYE")




