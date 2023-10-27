import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = [int(input()) for _ in range(n)]
left_res =lst[0]; right_res = lst[-1]
left_count = 1; right_count = 1;
for i in range(1,n):
    if lst[i] > left_res:
        left_res = lst[i]
        left_count += 1
for i in range(n,0,-1):
    if lst[i-1] > right_res:
        right_res = lst[i-1]
        right_count += 1
print(left_count, right_count,sep = "\n")