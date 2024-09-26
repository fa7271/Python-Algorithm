import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

black = []
white = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            # 짝수
            if (i + j) % 2 == 0:
                black.append((i, j))
            else:  # 홀수 칸
                white.append((i, j))

def is_possible(x, y, right, left):
    # 대각선 체크
    if not right[x+y] and not left[x-y+n-1]:
        return True
    return False
def bt(spots, index, right, left):
    if index == len(spots):
        return 0

    x, y = spots[index]
    max_count = bt(spots, index + 1, right, left)  # 비숍을 놓지 않는 경우

    if is_possible(x, y, right, left):  # 비숍을 놓을 수 있는 경우
        right[x + y] = True
        left[x - y + n - 1] = True
        max_count = max(max_count, 1 + bt(spots, index + 1, right, left))
        right[x + y] = False
        left[x - y + n - 1] = False

    return max_count

right_black = [False] * (2 * n - 1)
left_black = [False] * (2 * n - 1)
right_white = [False] * (2 * n - 1)
left_white = [False] * (2 * n - 1)

b = bt(black, 0, right_black, left_black)
w = bt(white, 0, right_white, left_white)

