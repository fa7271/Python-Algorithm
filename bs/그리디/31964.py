import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


1.
N = int(input())
X = [0, *map(int, input().split(" "))]
T = [0, *map(int, input().split(" "))]

# 최솟값
res = 2 * X[-1]

for i in range(1, N + 1):
    res = max(res, T[i] + X[i])

print(res)


2.
N = int(input())
X = list(map(int, input().split()))
T = list(map(int, input().split()))

houses = sorted(zip(X, T), reverse=True)
time = 0  # 현재 시간
pos = 0   # 현재 위치
for x, t in houses:
    time += abs(pos - x)
    # 물건이 안나옴
    if time < t:
        # 물건 나오는 시간 까지 기다림
        time = t
    pos = x

time += abs(pos - 0)
