import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())
def fibo(x):
    if x <= 1:
        return 1
    return x * fibo(x-1)

print(fibo(N))

