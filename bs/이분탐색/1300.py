import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, K = int(input()), int(input())

start = 1; end = K
res = 0
while start <= end:
    # middle 값
    mid = (start + end) // 2
    temp = 0
    # 각 행마다 mid 숫자보다 작은 갯수 temp에 다 더함
    for i in range(1, N+1):
        temp += min(mid // i, N)
    # 갯수가 많으면 줄여줌
    if temp >= K:
        res = mid
        end = mid-1
    else:
        start = mid +1
print(res)