import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

N,M = map(int,(input().split()))
jack = list(map(int,input().split()))

res = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if jack[i]+jack[j]+jack[k] > M:
                continue
            else:
                res = max(res,jack[i]+jack[j]+jack[k])
print(res)









