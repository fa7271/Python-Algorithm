import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, K = map(int,sys.stdin.readline().split(" "))
lst = list(map(int,sys.stdin.readline().split(" ")))

count = [0] * 100001
left, right = 0,0
res = 0

while right < N:
    if count[lst[right]] < K:
        count[lst[right]] +=1
        right +=1
    else:
        count[lst[left]] -= 1
        left += 1
    res = max(res, right-left)
print(res)