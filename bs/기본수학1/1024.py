import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

for i in range(m, 101):
    # 공차 1 등차수열 합
    x = n - (i * (i + 1) // 2)
    if x % i == 0:  # 등차수열 만족 했을때
        xx = x // i  # 연속된 자연수의 시작점
        if xx + 1 >= 0:
            print(*[i for i in range(xx + 1, xx + i + 1)])
            break
else:
    print(-1)
