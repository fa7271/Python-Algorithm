import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())
time = [list(map(int,sys.stdin.readline().rstrip().split(" "))) for i in range(N)]

time.sort(key = lambda x:(x[1],x[0]))
count = 0
idx = 0
for i in time:
    if i[0] >= idx :
        idx = i[1]
        count += 1
print(count)
