import sys
sys.stdin = open('/Python/h.txt', 'r')
input = sys.stdin.readline

N = int(input())
list = [0,1]

for i in range(2,N+1):
    list.append(list[i-1] + list[i-2])
print(list[N])


