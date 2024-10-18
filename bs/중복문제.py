import heapq
import sys
import re

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

a, b = map(int, input().split())

m = int(input())

arr = list(map(int, input().split()))
arr.reverse()
ten = 0
for i in range(m):
    ten += arr[i] * (a ** i)

result = []
while ten // b:
    result.append(ten % b)
    ten = ten // b
result.append(ten)
result.reverse()
print(' '.join(map(str, result)))
