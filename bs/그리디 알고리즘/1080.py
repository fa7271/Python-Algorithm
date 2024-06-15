import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

initial_value = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
target_value = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

count = 0


def change_value(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            initial_value[i][j] = 1 - initial_value[i][j]


for x in range(n - 2):
    for y in range(m - 2):
        if initial_value[x][y] != target_value[x][y]:
            change_value(x, y)
            count += 1
if initial_value == target_value :
    print(count)
else:
    print(-1)