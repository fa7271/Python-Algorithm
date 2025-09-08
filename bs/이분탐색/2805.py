import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N,M = map(int, (input().split()))    # 나무의 수 N, 필요한 나무의 길이 M
height = list(map(int, input().split()))
start, end = 1, max(height)
while start <= end:
    mid = (start + end) // 2
    count = [tree - mid if tree > mid else 0 for tree in height]
    # count = []
    # for tree in height:
    #     if tree > mid :
    #         count.append(tree - mid)
    #     else:
    #         count.append(0)

    res = sum(count)
    print(mid,res,start,count)
    if res >= M:
        start = mid +1
    else:
        end = mid - 1

print(end)

