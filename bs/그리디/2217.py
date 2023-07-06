import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(sys.stdin.readline())
lst = sorted([int(sys.stdin.readline().rstrip()) for i in range(N)], reverse= True)

res = []
idx = 1
for i in range(N):
    res.append(lst[i]*idx)
    idx += 1
print(max(res))
