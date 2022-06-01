import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

input = sys.stdin.readline


import math

# fac_a = math.factorial(int(input()))
# list_fac_a = list(map(int,str(fac_a)))

list_fac_a = list(map(int,str(math.factorial(int(input())))))
list_fac_a.reverse()
res = 0

for i in list_fac_a:
    if i == 0:
        res += 1
    if i != 0:
        break
print(res)