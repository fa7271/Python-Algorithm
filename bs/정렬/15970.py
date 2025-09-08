import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
arr = [[] for _ in range(n)]
for _ in range(n):
    a, b = map(int, input().split())
    arr[b-1].append(a)
res = 0

for i in arr:
    i.sort()
    if len(i) <= 1: continue
    res += abs(i[0] - i[1]) + abs(i[-1] - i[-2]) # 2 개의 점 왔다 갔다.
    for j in range(1, len(i) - 1): # 3개인 경우 가운데점 기준 왼쪾 오른쪽 중에 짧은거
        res += min(abs(i[j] - i[j - 1]), abs(i[j] - i[j + 1]))
print(res)
