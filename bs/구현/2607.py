import sys
import collections

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
target = input().strip()
words = [input().strip() for _ in range(N - 1)]

res = 0

for i in words:
    # 길이 1차이 이상나거나, 요소 2개이상 다르면 시도조차안됨
    if abs(len(i) - len(target)) > 1 or len(set(target).difference(set(i))) > 1: continue
    # 한 번만 제거함
    for j in target:
        if j in i:
            i = i.replace(j, "", 1)
    if len(i) <= 1:
        res += 1
print(res)
