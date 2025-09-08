import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, K = map(int,input().split(" "))

lst = sorted([int(str(i*N)[::-1]) for i in range(1,K+1)])
print(lst[-1])




