import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
s = sorted([list(map(int,input().split(" "))) for _ in range(n)], key = lambda x:x[1])
# [걸리는시간, 끝내야 하는 시간]

print(s)
res = 0
result = 1e9
for time, limit in s:
    res += time
    result = min(result, limit-res) #limit - res를 계산하여 현재 일을 제 시간에 끝낼 수 있는 가장 늦은 시간을 찾습니다
    if limit < res:
        print(-1)
        exit()
print(result)



