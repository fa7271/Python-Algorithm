def solution(m, n, board):
    b = list(map(list, zip(*board)))

    for i in range(m):
        board[i] = list(board[i])
    count = 0
    set_pop = set() # 공통으로 터지는 부분 방지
    while True:
        for x in range(m-1):
            for y in range(n-1):
                now = board[x][y]
                if now == []:
                    continue
                if board[x+1][y] == now and board[x][y+1] == now and board[x+1][y+1] == now: # 정사각형안에 캐릭터들 같을경우
                    set_pop.add((x,y)),set_pop.add((x+1,y)) # set 에 넣어줌
                    set_pop.add((x,y+1)),set_pop.add((x+1,y+1))
        if set_pop: # 겹치는 캐릭터들 제거 / count 추가
            count += len(set_pop)
            for i,j in set_pop:
                board[i][j] = []
            set_pop = set()
        else:
            return count

        while True:
            flag = True
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j]==[]:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        flag = False
            if flag:
                break
    return count
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
