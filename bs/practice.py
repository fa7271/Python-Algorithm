# import sys, heapq
# sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
#
# input = sys.stdin.readline
# V, E = map(int,input().split()) # 점 5개 간선 6개
# start = int(input()) # 시작점 1
# graph =[[] for _ in range(V+1)]
# dist = [float('inf')] * (V+1)
# dist[start] = 0
#
# for i in range(E):
#     u,v,w = map(int,input().split())
#     graph[u].append((v,w))
#
# heap = []
# heapq.heappush(heap,(0,start))
#
# while heap:
#     cur_w, cur_node = heapq.heappop(heap)
#
#     for to_node, to_w in graph[cur_node]:
#         dis = cur_w + to_w
#         if dis < dist[to_node]:
#             dist[to_node] = dis
#             heapq.heappush(heap,(dis, to_node))
#
# for i in dist[1:]:
#     print(i if i!=float('inf') else 'INF')

def get_divisor(n):
    data = []
    count =0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            data.append(i)
    data.append(n)
    return data


def solution(nubmers, target):
    res = [0]
    for i in nubmers:
        lst = []
        for j in res:
            lst.append(j+i)
            lst.append(j-i)
        res = lst
    return res.count(target)
# print(solution([4, 1, 2, 1], 4))


from collections import deque
def bfs (numbers, target):

    res = 0
    q = deque

    number_len = len(numbers)
    q.append([-numbers[0], 0] )
    q.append([+numbers[0], 0] )

    while q:
        x, y = q.popleft()
        if y == number_len -1 :
            if target == x:
                res +=1
        else:
            q.append([x - numbers[y+1], y+1])
            q.append([x - numbers[y+1], y+1])
    return res

# print(solution([4, 1, 2, 1], 4))
import heapq as hq

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    distance = [float("inf") for _ in range(N+1)]
    distance[1] = 0
    for start,end,cost in road:
        graph[start].append([end,cost])
        graph[end].append([start,cost])
    heap  = []
    hq.heappush(heap,(0,1))
    while heap:
        cost,curr = hq.heappop(heap)
        if distance[curr] < cost:
            continue
        for nxt,c in graph[curr]:
            totalCost = cost + c
            if totalCost < distance[nxt]:
                print(totalCost, distance[nxt])
                distance[nxt] = totalCost
                hq.heappush(heap,(totalCost,nxt))
    for i in distance[1:]:
        if i <= K:
            answer += 1
    return answer

print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))





