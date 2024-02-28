import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))), reverse=True)
count = sum(lst) // 3
if sum(lst) % 3 != 0:
    print("NO")
else:
    for a in lst:
        count -= a//2
    if count > 0:
        print("NO")
    else:
        print("YES")
