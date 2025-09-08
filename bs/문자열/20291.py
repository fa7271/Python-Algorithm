import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(input())
lst =[input().split(".") for _ in range(t)]
dic = defaultdict(int)

for i in lst:
    dic[i[1]] += 1
for i in sorted(dic.items()):
    print(*i)


