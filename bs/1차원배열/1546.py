import sys
sys.stdin = open('/Python/h.txt', 'r')



n = int(input())
a = list(map(int,input().split()))
m = int(max(a))
sum = 0
for i in range(n):
    a[i] = a[i]/m*100
    sum += a[i]
print(sum/n)
