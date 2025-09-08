import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(sys.stdin.readline())
res = 0
cnt =0
for i in range(1,N+1):
    res += i
    cnt += 1
    if res > N:
        cnt -=1
        break

print(cnt)


