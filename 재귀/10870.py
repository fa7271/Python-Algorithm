import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')
input = sys.stdin.readline

N = int(input())
list = [0,1]

for i in range(2,N+1):
    a = list[i-1] + list[i-2]
    list.append(a)
print(list[N])


