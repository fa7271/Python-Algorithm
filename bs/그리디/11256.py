import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(input())
result = []
for i in range(t):
    count = 0
    j, n = map(int, sys.stdin.readline().split(" "))
    res = sorted([x*y for x, y in [list(map(int, input().rstrip().split(" "))) for _ in range(n)]], reverse=True)
    for i in res:
        j -= i
        count += 1
        if j <=0 :
            break
    result.append(count)
print(*result,sep='\n')

