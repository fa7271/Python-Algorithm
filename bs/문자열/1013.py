
import sys
import re
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# (100+1+ | 01)+

t = int(input())

for x in range(t):
    word = input().rstrip()
    p = re.compile('(100+1+|01)+')
    flag = p.fullmatch(word) # match 로 하면 한개만 맞춤, fullmatch 필요
    if flag:print("YES")
    else:print("NO")

