import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


def dfs(x,y,z):
    global answer
    now = board[x][y]

    for i in range(x, x+z):
        for j in range(y, y+z):
            if now != board[i][j]: # 1개까지 dfs돌고 1개일때 여기서 걸리면서
                for k in range(3):
                    for l in range(3):
                        dfs(x + k*z//3, y + l*z//3, z//3)
                return
    # 여기서 체크해주고 리턴함
    if now == -1:
        answer[0] += 1
    elif now == 0:
        answer[1] += 1
    else:
        answer[2] +=1

n = int(sys.stdin.readline())
board= [list(map(int,sys.stdin.readline().split(" "))) for _ in range(n)]
answer = [0,0,0]
dfs(0,0,n)
[print(res) for res in answer]

