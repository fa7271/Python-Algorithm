import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

input = sys.stdin.readline
# input = int(sys.stdin.readline())


def get(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5


w, h, x, y, p = map(int, input().split())  # h짝수
ans = 0

for _ in range(p):
    a, b = map(int, input().split())
    if x <= a <= x + w and y <= b <= y + h:  # 직사각형 안일떄
        ans += 1
        continue

    r = h / 2

    if get(x, y + r, a, b) <= r or get(x + w, y + r, a, b) <= r:
        ans += 1
print(ans)
