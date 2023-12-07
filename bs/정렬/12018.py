import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n, m = map(int, sys.stdin.readline().split())
result = []
for _ in range(n):
    p, l = map(int,sys.stdin.readline().split())
    score = sorted(list(map(int,sys.stdin.readline().split(" "))), reverse=True)
    if p < l:
        result.append(1)
    else:
        result.append(score[l-1])
result.sort()
count = 0
for i in result:
    m -= i
    count += 1
    if m < 0:
        print(count - 1)
        break

if m > 0:
    print(count)
