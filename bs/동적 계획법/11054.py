import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())
lst = [int(i) for i in sys.stdin.readline().split(" ")]
dp_max = [1] * N
dp_min = [1] * N
left = []

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp_max[i] = max(dp_max[i], dp_max[j] + 1)
lst.reverse()
for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp_min[i] = max(dp_min[i], dp_min[j] + 1)
dp_min.reverse()

res = 0
for i in range(N):
    res = max(res,dp_max[i]+dp_min[i])
print(res-1)