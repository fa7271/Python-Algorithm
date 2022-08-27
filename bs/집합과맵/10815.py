import sys
sys.stdin = open('/Python/h.txt', 'r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())



n = int(input())

arr = set(map(int, input().split()))
n2 = int(input())
arr2 = list(map(int, input().split()))
res = []
for i in arr2:
    if i in arr:
        res.append(1)
    else:
        res.append(0)
print(*res)


