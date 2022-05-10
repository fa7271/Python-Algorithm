import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')


a = int(input())
b = int(input())
c = int(input())

d = list(map(int,str(a*b*c)))

for i in range(10):
    print(d.count(i))


