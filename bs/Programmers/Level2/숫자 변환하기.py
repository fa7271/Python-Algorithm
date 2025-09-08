from collections import deque


def solution(x, y, n):
    def bfs(x, y, n):
        q = deque()
        board[x] = 1
        q.append(x)

        while q:
            x = q.popleft()
            if 0 <= x + n <= 1000000 and board[x + n] == 0:
                board[x + n] = board[x] + 1
                q.append(x + n)
            if 0 <= x * 2 <= 1000000 and board[x * 2] == 0:
                board[x * 2] = board[x] + 1
                q.append(x * 2)
            if 0 <= x * 3 <= 1000000 and board[x * 3] == 0:
                board[x * 3] = board[x] + 1
                q.append(x * 3)

    board = [0] * 1000001
    bfs(x,y,n)

    return board[y]-1
print(solution(10,40,30))
def solution2(x, y, n):

    count = 0
    answer = set()
    answer.add(x) # 시작값 x 10 넣음

    while answer:
        if y in answer:
            return count

        nx_answer = set()
        for nx in answer:
            if nx + n <= y:
                nx_answer.add(n+nx)
            if nx * 2 <= y:
                nx_answer.add(2*nx)
            if nx * 3 <= y:
                nx_answer.add(3*nx)
        answer = nx_answer
        count += 1
    return -1

print(solution2(10,40,30))
