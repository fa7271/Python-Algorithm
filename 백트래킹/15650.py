import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


# from itertools import combinations
#
# N, M = map(int, input().split())
#
# p = combinations(range(1, N+1), M)
# for i in p:
#     print(*i)


n,m = map(int,input().split())
visited = [False] * n
result = []

def solve(num):
    if num == m:
        print(*result)
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result.append(i + 1)
            solve(num+1)
            result.pop()
            for j in range(i+1, n):
                visited[j] = False

solve(0)

