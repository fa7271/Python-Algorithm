import sys
from collections import Counter
from itertools import permutations, combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

temp = list(map(str, input()))
temp = Counter(temp)

checkCount = 0
mid = ''
for key, value in list(temp.items()):
    # 홀수면 미드값
    if value % 2:
        checkCount += 1
        mid = key
        if checkCount > 1:
            print("I'm Sorry Hansoo")
            exit()
res = ''
for key, value in sorted(temp.items()):
    # 절반
    res += (key * (value // 2))
res = res + mid + res[::-1]
print(res)
