import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n,m = map(int,input().split())
visited = [False] * n
result = []
def solve(num):
    if num == m:
        print(*result)
        return

    for i in range(n):
        if visited[i] == False:
            # visited[i] = True
            result.append(i + 1)
            solve(num+1)
            visited[i] = True
            result.pop()
            for j in range(i+1, n):
                visited[j] = False

solve(0)

def bt(num):
    if len(result) == m:
        print(*result)
        return

    for i in range(num, n+1):
        result.append(i)
        bt(i)
        result.pop()

bt(1)
