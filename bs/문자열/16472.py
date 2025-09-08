import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
word = list(map(str,sys.stdin.readline()))
# 최대 N개의 종류의 알파벳을 가진 연속된 문자열

# two pointer
start = 0
res = 0
dic = defaultdict(int)

for right in range(len(word)):
    dic[word[right]] += 1
    while len(dic) > n:
        dic[word[start]] -= 1
        # 제거
        if dic[word[start]] == 0:
            del dic[word[start]]
        start += 1
    res = max(res, right - start + 1)
print(res)
