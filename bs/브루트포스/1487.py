import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
left = []
right = []
for i in range(n):
    x,y = map(int,input().split())
    left.append(x)
    right.append(y)


max_m = 0
ans = 0
for i in sorted(left):
    money = 0
    for j in range(n):
        if i <= left[j] and i > right[j]:
            money += i - right[j]
    if max_m < money:
        max_m = money
        ans = i

print(ans)