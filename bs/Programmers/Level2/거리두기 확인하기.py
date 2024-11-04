from itertools import combinations


def solution(places):

    answer = []
    board = [[list(map(str, j)) for j in places[i]] for i in range(len(places))]
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'P':
                board[i][j] = 'X'
    def find(x, y):
        for dx, dy in move:
            nx = dx + x[0]
            ny = dy + x[1]
            # 이동 했을때 P 일경우
            if nx == y[0] and ny == y[1]:
                return False

    for maps in board:
        P_com = []
        for x in range(5):
            for y in range(5):
                if maps[x][y] == 'P':
                    P_com.append((x,y)) # P값 뽑음

        # 2개 뽑아서 조합 만들어줌, > 맨해튼 거리 구해야 하기 때문에
        combi = combinations(P_com,2)

        # 의심되는 값 넣어줌
        doubt_res = []
        for com in combi:
            # 맨해튼 거리 2 이하면 일단 의심해야함
            if abs(com[0][0] - com[1][0]) + abs(com[0][1]-com[1][1]) <= 2:
                doubt_res.append(com)
        # 두 점 가능한지 체크
        for x, y in doubt_res:
            flag = find(x, y)
            if flag == False:
                answer.append(0)
                continue
        break

#  (r1, c1), (r2, c2)
#  |r1 - r2| + |c1 - c2|


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# 파티션 사이에 사람 거리두기 o 좌우로
# 사람 대각선 거리두기 o
# 책상 끼고 사람 거리두기 x


# 사람기준
# idea
#  사람기준 네 방향 체크,
#  책상 있을시 책상기준 네 방향 사람 체크.
# 대각선 일때 대각선 노드 그 사이 값들 파티션 없으면 안됨.

# 1. P값 조합 2개 뽑아서, 거리 2 이하인 것들만 보아놓음

# 지켰으면 1, 안 지켰으면 0
# 맨해튼 거리 2 이하 > 8가지 방향,