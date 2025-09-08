import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
dic = defaultdict()
lst = [input() for _ in range(n)]
for i in lst:
    cnt = len(i)
    for j in i:
        if j not in dic:
            dic[j] = (10 ** (cnt - 1))
        else:
            dic[j] += (10 ** (cnt - 1))
        cnt -= 1

x = sorted(dic.items(), key=lambda x: -x[1])
res = 0
mul = 9
for i in x:
    res += i[1] * mul
    mul -= 1
print(res)
