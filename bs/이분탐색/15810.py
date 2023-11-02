import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int,input().split())
A = sorted(list(map(int,input().split())))
start = 0; end = A[-1] * m
res = 0
while start <= end:
    mid = (start + end) //2

    # 최소 시간 초과 될때
    if sum(mid//i for i in A) >= m:
        res = mid
        end = mid - 1
    else:
        start = mid +1
print(res)

