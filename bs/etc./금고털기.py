import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

w, n = map(int,sys.stdin.readline().split(" "))

arr = sorted([list(map(int,sys.stdin.readline().split(" "))) for _ in range(n)], key = lambda x:-x[1])
res = 0
for i in arr:
    if w >= i[0]:
        w -= i[0]
        res += i[0] * i[1]
    else:
        res += w * i[1]
        break
print(res)