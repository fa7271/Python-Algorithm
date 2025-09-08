import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n,m = map(int,input().split())
x =sorted(list(map(int,input().split())))
visited = [False] * n
result = []


def bt():
    if len(result) == m:
        print(*result)
        return
    number = 0
    for i in range(n):
        if not visited[i] and number != x[i]:
            visited[i] = True
            result.append(x[i])
            number = x[i]
            bt()
            visited[i] = False
            result.pop()
bt()
