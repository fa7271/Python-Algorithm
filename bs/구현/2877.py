import sys
import itertools

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())

length = 1
count = 0

# 몇 자리 수인지 찾기
while True:
    if count + (2 ** length) >= n:
        break
    count += (2 ** length)
    length += 1

offset = n - count - 1


answer = ""
for i in range(length - 1, -1, -1):
    if offset & (1 << i):
        answer += "7"
    else:
        answer += "4"

print(answer)