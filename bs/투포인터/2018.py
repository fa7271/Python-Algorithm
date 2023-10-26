import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        n_sum = (i * j + (j - 1) * j // 2)
        if n == n_sum:
            cnt += 1
            break
        elif n < n_sum:
            break
print(cnt)