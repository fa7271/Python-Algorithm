import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# from itertools import combinations
#
# N, M = map(int, input().split())
#
# p = combinations(range(1, N+1), M)
# for i in p:
#     print(*i)


n,m = map(int,input().split())
# visited = [False] * n
result = []

# def solve(num):
#     if num == m:
#         print(*result)
#         return
#
#     for i in range(n):
#         if visited[i] == False:
#             # visited[i] =True            #  방문여부 체크인데 중복 가능이니 필요없음
#             result.append(i + 1)
#             solve(num+1)
#             # visited[i] = False
#             result.pop()
#             # for j in range(0,n):
#             #     visited[i] = False
# solve(0)

# 중복이 가능므로 빅오 O(N^2) (10개 까지 가능)

def bt(num): # n = 4 m = 2
    if len(result) == m:
        print(*result)
        return
    for i in range(1,n+1):
        result.append(i)
        bt(i+1)
        result.pop()

bt(0)
