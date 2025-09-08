import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))


start = max(lst)
end = sum(lst)
res = 0
while start <= end:
    middle = (start + end) // 2
    blueray = 1
    temp = 0
    for i in lst:
        if temp + i > middle:
            blueray += 1
            temp = 0
        temp += i
    if blueray <= m:
        res = middle
        end = middle -1
    else:
        start = middle+1

print(res)
