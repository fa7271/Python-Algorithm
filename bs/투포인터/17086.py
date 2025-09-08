import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, x = map(int, sys.stdin.readline().rstrip().split(" "))
arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
dic = defaultdict(int)
temp =0
for i in range(x):
    temp += arr[i]
dic[temp] = 1
left = 0 ; right = x-1
for i in range(1, n-x+1):
    temp -= arr[left]
    left += 1
    right +=1
    temp += arr[right]
    dic[temp] += 1
res = sorted(dic.items(), key=lambda x: -x[0])[0]
if res[0] == 0:
    print("SAD")
else:
    print(res[0], res[1], sep="\n")

