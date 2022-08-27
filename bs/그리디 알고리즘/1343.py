import sys
sys.stdin = open('/Python/h.txt', 'r')

input = sys.stdin.readline
# input = int(sys.stdin.readline())


arr =input().replace("XXXX","AAAA").replace("XX","BB")

if "X" in arr:
    print(-1)
else:
    print(arr)


