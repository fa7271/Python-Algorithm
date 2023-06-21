import sys
from collections import deque
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**8)

N,M = map(int,input().split()) # N은 격자 사이즈, M은 치킨집 개수
graph = []
house = []
chicken = []

for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split(" "))))
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i,j))
        if graph[i][j] == 2:
            chicken.append((i,j))

arr = []
res = int(1e9)
def dfs(num, cnt):
    global res
    if num >len(chicken):# 현재 선택한 치킨집의 개수가 전체 치킨집의 개수를 초과
        return
    if cnt == M:
        total = 0
        for x, y in house:
            dist = int(1e9)
            for idx in arr:
                k, l = chicken[idx]
                dist = min(dist,abs(x-k)+abs(y-l))
            total += dist
        res =min(total,res)
        return
    arr.append(num)
    dfs(num+1,cnt+1)
    arr.pop()
    dfs(num+1,cnt)
    return res

print(dfs(0,0))

# arr = []
# real_check = int(1e9)
# def back(num,cnt):
#     global real_check
#     if num > len(chicken):
#         return
#     if cnt==M:
#         result_tot = 0
#         for hx,hy in house:
#             min_check = int(1e9)
#             for idx in arr:
#                 cx,cy = chicken[idx]
#                 min_check = min(min_check,abs(hx-cx)+abs(hy-cy))
#
#             result_tot += min_check
#
#         real_check = min(result_tot,real_check)
#         return
#     arr.append(num)
#     back(num+1,cnt+1)
#     arr.pop()
#     back(num+1,cnt)
#     return real_check
#
# print(back(0,0))
#

# def dfs():

