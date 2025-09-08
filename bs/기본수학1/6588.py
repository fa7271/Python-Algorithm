import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = [True] * 1000001  # 숫자범위

# 소수 리스트
for i in range(2, int((len(N) ** 0.5) + 1)):
    if N[i]:
        for k in range(2 * i, 1000001, i):
            N[k] = False
# b-a가 가장 큰 것
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    for i in range(3, n - 2, 2):
        if N[i] and N[n - i]:
            print(n, "=", i, "+", n - i)
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')
