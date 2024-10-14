import heapq
import sys
import re

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

x = list(input())
dic = {chr(i) : 0 for i in range(97, 123)}
for i in x:
    dic[i] += 1
print(*list(dic.values()))
