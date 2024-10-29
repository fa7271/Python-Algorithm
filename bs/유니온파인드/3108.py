import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


# 겹치는지 확인하는 함수
def is_overlapping(x1_1, y1_1, x2_1, y2_1, x1_2, y1_2, x2_2, y2_2):
    # 한 직사각형이 다른 직사각형을 완전히 포함하는 경우 겹치지 않는 것으로 간주
    if (x1_1 < x1_2 and y1_1 < y1_2 and x2_1 > x2_2 and y2_1 > y2_2) or \
            (x1_2 < x1_1 and y1_2 < y1_1 and x2_2 > x2_1 and y2_2 > y2_1):
        return False

    # 기본 겹침 여부 확인
    if x2_1 < x1_2 or x1_1 > x2_2 or y2_1 < y1_2 or y1_1 > y2_2:
        return False
    else:
        return True


n = int(input())
graph = [[] for _ in range(n)]
rectangles = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
parent = [i for i in range(n)]

start_zero = False
# 0,0 에서 갈 수 있는거 찾음
for rectangle in rectangles:
    a, b, c, d = rectangle
    if a == 0 or c == 0:
        if b <= 0 <= d:
            start_zero = True
    elif b == 0 and d == 0:
        if a <= 0 <= c:
            start_zero = True


def find(i):
    if i != parent[i]:
        parent[i] = find(parent[i])
    return parent[i]


def union(a, b):
    aa = find(a)
    bb = find(b)
    if aa < bb:
        parent[bb] = aa
    else:
        parent[aa] = bb


for i in range(n - 1):
    for j in range(i + 1, n):
        if is_overlapping(*rectangles[i], *rectangles[j]):
            # 몇 번 째 사각형끼리 union인지
            union(i, j)
cnt = 0
for i in range(n):
    if parent[i] == i:
        cnt += 1
if start_zero:
    cnt -= 1
print(cnt)
