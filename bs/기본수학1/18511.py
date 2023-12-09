import sys
from itertools import  product

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k =map(int,sys.stdin.readline().split(" "))
lst = list(map(int,sys.stdin.readline().split(" ")))
res =[-1]
for lens in range(1,len(str(n))+1):
    for num in list(product(lst, repeat = lens)):
        if n >= int(''.join(map(str, num))):
            res.append(int(''.join(map(str, num))))
print(max(res))

