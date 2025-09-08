import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**6)

def fac(N, rest):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % rest
    return n

# 거듭제곱 계산 (나머지 연산 적용)
def reduce_pow(a, b, c):
    if (b == 1):
        return a % c

    X = reduce_pow(a, b//2, c)

    if (b % 2 == 0): # 짝수라면
        return X * X % c
    else: # 홀수라면
        return a * X * X % c


N, K = map(int, input().split())
P = 1000000007

TOP = fac(N, P)

BOTTOM = fac(K, P) * fac(N-K, P)

print(TOP * reduce_pow(BOTTOM , P-2, P) % P)
