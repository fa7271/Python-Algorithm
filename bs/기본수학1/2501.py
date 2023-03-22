import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, K = list(map(int,input().split(" ")))

les = []
for i in range(1,N+1):
    if N% i ==0 :
       les.append(i)
if K > len(les):
    print(0)
else:
    print(les[K-1])



