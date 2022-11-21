import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
N =int(input())
col = [0] * (N+1)
count =0
def N_Queen(col, i):
    n =len(col) -1
    if promising(col, i):
        if i == n:
            global count
            count += 1
        else:
            for j in range(1, n+1): # 다음 행 체크하려고 (1,3) 왔을때 2,1 / 2,2/ 2,3/ 2,4 체크
                col[i+1] = j # 다음행 추가(1,3,1)\/ (1,3,2) 이런식
                N_Queen(col,i+1)
def promising(col, i):
    k = 1
    flag = True
    while (k < i and flag): # k 가 i 보다 작고 True일때
        if (col[i] == col[k] or abs(col[i]-col[k]) == (i-k)): # 같은 col에 있느냐, 같은대각선이냐
            flag = False # 있으면 false
        k += 1
    return flag

N_Queen(col,0)

print(count)

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
