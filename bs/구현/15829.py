import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
word = str(input())
res = 0
temp = 31
idx = 0
for i in word:
    x = ord(i) - 96
    res += x * (temp**idx)
    idx += 1
print(res%1234567891)