import sys
# sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

K,N = map(int,(input().split()))    # 이미 가지고 있는 랜선의 개수 K, 필요한 랜선의 개수 N
line = [int(input()) for i in range(K)]
start, end = 1, max(line)

while start <= end:
    mid = (start + end) // 2
    res = 0 # 필요한 라인 수

    for i in line:
        res += i // mid
    if res >= N:
        start = mid+1
    else:
        end = mid-1

print(end)
