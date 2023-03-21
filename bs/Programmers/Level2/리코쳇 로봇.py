from collections import deque

def solution(board):
    visited = [[0] * len(board[0]) for i in range(len(board))]
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = set()
    Q = deque()

    for idx, i in enumerate(board):
        for idy, j in enumerate(i):
            if board[idx][idy] == "R":
                Q.append((idx,idy,0))


    while Q:
        x, y, count = Q.popleft()
        if (x,y) in visited:
            continue
        if board[x][y] == "G": # 탈출조건
            return count
        visited.add((x,y))
        for nx, ny in move:
            now_x, now_y = x, y
            while True:
                next_x, next_y = now_x + nx, now_y + ny
                if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]) and board[next_x][next_y] != "D":
                    now_x, now_y = next_x, next_y
                    continue
                Q.append((now_x,now_y, count+1 ))
                break
    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
# print(solution(	[".D.R", "....", ".G..", "...D"]))