import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
num = list(map(int, sys.stdin.readline().split(" ")))

res = []
result = -1e9

visited = [False] * n

def bt():
    global result

    if len(res) == n:
        result = max(sum(abs(res[i] - res[i+1]) for i in range(n-1)),result)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            res.append(num[i])
            bt()
            visited[i] = False
            res.pop()
bt()
print(result)

