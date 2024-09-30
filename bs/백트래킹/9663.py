import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
import sys


n = int(input())
res = 0
lst = [0] * n


def is_possible(x):
    for i in range(x):
        if lst[i] == lst[x] or abs(x-i) == abs(lst[x]-lst[i]):
            return False
    return True


def bt(i):
    global res
    if i == n:
        res += 1
        return
    for j in range(n):
        lst[i] = j
        if is_possible(i):
            bt(i+1)
        lst[i] = 0
bt(0)
print(res)
# def dfs(depth):
#     global count
#     if depth == N:
#         count += 1
#         return
#
#     for i in range(N):
#         if visited[i]==0: # 해당 자리에 퀸이 존재하는지 확인
#
#             graph[depth] = i # 각 행마다 위치하는 퀸의 자리
#
#             t=True
#             for j in range(depth):   # graph의 개수만큼 for문을 돌려야하지만 어차피 depth랑 개수 똑같음
#                 if abs(graph[depth]-graph[j])==abs(depth-j):
#                     t=False
#                     break
#             if t:
#                 visited[i] = 1
#                 dfs(depth+1)
#                 visited[i] = 0
#
#
# graph = [0]*N
# visited = [0]*N
#
# count= 0
# dfs(0)
# print(count)
