import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(sys.stdin.readline())
arr = [(i, int(sys.stdin.readline())) for i in range(n)]
arr2 = sorted(arr, key=lambda x: x[1])
res = 0
print(arr, arr2,sep="\n")
for i in range(n):
    print(arr2[i][0] - i)
    res = max(arr2[i][0] - i, res)
print(res)
