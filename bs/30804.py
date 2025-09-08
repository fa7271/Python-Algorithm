import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
length = 0
dic = defaultdict(int)
res = 0
while right < N:
    if dic[lst[right]] == 0:
        length += 1
    dic[lst[right]] += 1
    while length > 2:
        dic[lst[left]] -= 1
        if dic[lst[left]] == 0:
            length -= 1
        left += 1
    res = max(res, right - left + 1)
    right += 1
print(res)
