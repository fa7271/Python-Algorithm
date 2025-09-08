import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, input().split())
interest = [list(map(int, input().split())) for _ in range(n)]
like = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]
graph = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
def check():
    for a, b, t in graph:
        if interest[visited[a]][t] != interest[visited[b]][t]:
            return False

    return True
def bt(depth):
    if depth == n:
        if check():
            print('YES')
            print(*[i + 1 for i in visited])
            exit()
        return

    for i in range(len(like[depth])):
        tmp = like[depth][i]
        if visited[tmp] == -1:
            visited[tmp] = depth
            bt(depth + 1)
            visited[tmp] = -1


visited = [-1] * n

bt(0)
print('NO')