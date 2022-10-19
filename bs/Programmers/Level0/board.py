def solution(board):
    board_True = [[0 for col in range(len(board))] for row in range(len(board))]
    mine = 0
    for x in range(0, len(board)):
        for y in range(0,len(board[0])):
            if board[x][y] == 1:
                if x == 0 and 1 <= y < len(board): # 맨 윗줄 맨 아랫줄
                    board_True[x][y-1:y+2] = "False","False","False"
                    board_True[x+1][y-1:y+2] = "False","False","False"     #down
                # elif y == 0 and 1<= x < len(board): # 맨 왼쪽줄 맨 오른쪽 줄
                #     board_True[x-1:x+2][y] = "False","False","Falsse"
                #     board_True[x-1:x+2][y+1] = "False","False","False"
                # elif x == 0 and y == 0 : #왼쪽위
                #     board_True[x][y:y+2] = "False","False"
                #     board_True[x+1][y:y+2] = "False"
                # elif x == 0 and y == 4 : # 왼쪽아래
                #     board_True[x][y-1:y+1] = "False","False"
                #     board_True[x+1][y-1:y+1] = "False","False"
                # elif x == 4 and y == 0 : #오른쪽위
                #     board_True[x][y:y+2] = "False","False"
                #     board_True[x-1][y:y+2] = "False"
                # elif x == 4 and y == 4 : # 왼쪽아래
                #     board_True[x][y-1:y+1] = "False","False"
                #     board_True[x-1][y-1:y+1] = "False","False"
                # else:
                #     board_True[x-1][y-1:y+2] = "False","False","False"     # up
                #     board_True[x][y-1:y+2] = "False","False","False"             #mid
                #     board_True[x+1][y-1:y+2] = "False","False","False"     #down
    return (len(board)*len(board)) - sum(board_True,[]).count('False') - mine

        # for y in board[0][1:]:
            # if y = 1:
            # if board[x][y] == 1:
            #     board_True[x][y] = "False"
            #     print(board_True)
    # print(board_True)

def solution(board):
    answer = 0

    for col in range(len(board)):
        for row in range(len(board[col])):
            if board[row][col] == 1:
                for j in range(max(col-1,0),min(col+2,len(board))):
                    for i in range(max(row-1,0),min(row+2,len(board))):
                        if board[i][j] == 1:
                            continue
                        board[i][j] = -1
    for i in board:
        answer += i.count(0)

    return answer

# 3,2
# print(solution( [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]] ))  # f 8 - m 1
print(solution( [[1,1,1], [1,0,0], [1,0,0]] ))  # f 8 - m 1
# print(solution( [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]] ))  # f 12 - m 2
# print(solution( [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]  ))  # f 12 - m 2
# print(solution( [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]] ))


