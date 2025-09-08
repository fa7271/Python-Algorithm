import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())

for i in range(N):
    res = []
    x = bin(int(input()))[::-1][:-2]
    for idx,j in enumerate(x):
        if j == "1":
            res.append(idx)
    print(*res)

