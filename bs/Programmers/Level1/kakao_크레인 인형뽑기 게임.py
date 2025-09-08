def solution(board, moves):
    stack = []
    res = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0: # 뽑는수가 0 이 아닐때
                stack.append(board[j][i-1]) # 뽑은 숫자 스택에 넣고
                board[j][i-1] = 0  # 뽑은수 0 으로 바꿔줌

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        res += 2
                break
    return res




print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4] ))
# result = 4

# 1. 마지막 원소를 빼서 새로운 스택에 넣기 //
# 2. 마지막꺼 0 으로 바꿔줌
# 3. 스택 길이 2 이상이면 맨 뒤랑 그 앞에꺼 비교