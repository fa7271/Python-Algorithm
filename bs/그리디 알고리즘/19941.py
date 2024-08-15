import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k = map(int, sys.stdin.readline().split())
word = [*map(str, sys.stdin.readline())]
res = 0
for i in range(n):
    if word[i] == "P":
        for ran in range(max(i - k, 0), min(i + k + 1, n)):
            if word[ran] == "H":
                word[ran] = 0
                res += 1
                break
print(res)