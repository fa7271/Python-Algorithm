import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())

word = [""] + [str(sys.stdin.readline().rstrip()) for _ in range(n)]
linked_list = [-1] * (n + 1)
tail = [i for i in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    linked_list[tail[x]] = y
    tail[x] = tail[y]
result = []
for _ in range(n):
    result .append(word[x])
    x = linked_list[x]
print("".join(result))
