from collections import deque


# def solution(n, costs):
#
#     costs = sorted(costs, key=lambda x:(x[2]))
#
#     dist =[1] + [0] * (n-1)
#     graph = [ [] for _ in range(n)]
#     for ( x, y, z ) in costs:
#         graph[x].append((y, z))
#         graph[y].append((x, z))
#     # graph = [()] 이차원 리스트에서 각 리스트 가는 방향과 값.
#     q = deque([0])
#     # print(graph,q,dist,sep="\n")
#     res = 0
#     while q:
#         l = len(q)
#         for i in range(l): # (0,1)
#             now = q.popleft()
#             for next_node, w  in graph[now]:
#                 if dist[next_node] == 0:
#                     dist[next_node] = 1
#                     q.append(next_node)
#                     res += w
#     return res
def solution1(n, costs):
    res = 0
    costs.sort(key = lambda x:x[2])
    connect = set([costs[0][0]])
    while len(connect ) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect: #연결 된 경우
                continue # 넘어간다.
            if cost[0] in connect or cost[1] in connect :
                connect.update([cost[0],cost[1]])
                res += cost[2]
    print(res)



def solution(n,consts):

    cost = sorted(consts,key = lambda x:x[2])
    parent = [i for i in range(n+1)]
    answer =0
    for x,y,z in cost:
        if find(parent,x) != find(parent,y):
            union(parent,x,y)
            answer += z
    return answer

def find(parent, x):
    if parent[x] != x: # 자기 자신이 아닌경우 다른 노드에 연결된 경우
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent,x,y):
    x = find(parent,x)
    y = find(parent,y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

# [[0, 1, 1], [1, 3, 1], [0, 2, 2], [1, 2, 5], [2, 3, 8]]

print(solution1(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
# print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])) # 11
# print(solution(7, [[2, 3, 7], [3, 6, 13], [3, 5, 23], [5, 6, 25], [0, 1, 29], [1, 5, 34], [1, 2, 35], [4, 5, 53], [0, 4, 75]])) # 11

# print(solution1(7,[[1,2,29],[1,6,75],[2,3,35],[2,6,34],[3,4,7],[4,6,23],[4,7,13],[5,6,53],[6,7,25]]))

[ 1, 1, 2, 3, 5, 1, 6]
[ 1, 1, 1, 3, 1, 1, 3]
