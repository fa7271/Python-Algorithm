import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())

board= [list(map(str,sys.stdin.readline().rstrip())) for _ in range(n)]
move = [(1, 0),(0, 1),(-1,0),(0,-1)] # 오른쪽, 아래
count = -1e9
temp =''
# (0,0) 부터 확인
for i in range(n):
    for j in range(n):
        for dx, dy in move:
            nx = dx + i
            ny = dy + j
            if 0 <= nx < n and 0 <= ny < n:
                if board[i][j] != board[nx][ny]:
                    # 바꿔줌
                    temp = board[i][j]
                    board[i][j] =board[nx][ny]
                    board[nx][ny] = temp
                x, y = 1, 1
                # 맞는거 확인
                for l in range(n-1):
                    # 가로
                    if board[i][l] == board[i][l+1]:
                        x += 1
                    else:
                        x = 1
                    if board[l][j] == board[l+1][j]:
                        y += 1
                    else:
                        y = 1
                    count = max(count, x, y)
                if board[i][j] != board[nx][ny]:
                    board[nx][ny] = board[i][j]
                    board[i][j] = temp
print(count)





# 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다.
# 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다.
# 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.