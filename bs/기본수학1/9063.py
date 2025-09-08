import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = sorted([list(map(int,sys.stdin.readline().split())) for _ in range(n)], key = lambda x:x[0])
x = lst[-1][0]- lst[0][0]
lst.sort(key = lambda x:x[1])
y = lst[-1][1]- lst[0][1]
if len(lst) <= 1:
    print(0)
    exit()

print(x * y)