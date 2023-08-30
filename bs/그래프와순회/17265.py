
import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')



# def dfs(x, y, curr_num, before):  # 좌표, 그때까지 계산한 값
#     global max_answer, min_answer
#
#     if x == N - 1 and y == N - 1:  # 학교 도착했으면
#         # 정답 업데이트
#         max_answer = max(max_answer, int(curr_num))
#         min_answer = min(min_answer, int(curr_num))
#
#     # 아래, 오른쪽만
#     for dx, dy in move:
#         nx = dx+ x
#         ny = dy + y
#         if 0 <= nx <N and 0 <= ny <N:
#             if maps[nx][ny].isdigit():  # 숫자라면
#                 dfs(nx, ny, str(eval(curr_num + before + maps[nx][ny])), '')
#             else:  # 기호라면
#                 dfs(nx, ny, curr_num, maps[nx][ny])
#

def dfs(x, y, res, before):
    global max_answer, min_answer

    if x == N-1 and y == N-1:
        max_answer = max(max_answer,int(res))
        min_answer = min(min_answer,int(res))
    for dx, dy in move:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < N and 0 <= ny < N:
            if maps[nx][ny].isdigit():
                print(type(res))
                dfs(nx,ny,eval(str(res) + before + maps[nx][ny]),"")
            else:
                dfs(nx,ny,res,maps[nx][ny])

N = int(input())
maps = list(input().split() for _ in range(N))
move = [(1,0),(0,1)]
max_answer = -1e9
min_answer = 1e9

dfs(0, 0, maps[0][0], '')
print(max_answer, min_answer)
