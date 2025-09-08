import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

K = int(sys.stdin.readline())


def hanoi(n, i, j, via):
    if n == 1:
        print(i,j)
    else:
        hanoi(n - 1, i, via, j)  # n-1개의 원반을 이웃한 기둥으로
        print(i, j)  # 가장큰거 최종으로
        hanoi(n - 1, via, j, i)  # 이웃한 기둥에서 n-1개의 원반을 최종 목적 기둥으로


if K <= 20:
    hanoi(K, 1, 3, 2)
