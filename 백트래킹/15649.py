import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# input = sys.stdin.readline
# # input = int(sys.stdin.readline())
#
# n, m = map(int, input().split())
# s = []
#
# def f():
#     if len(s) == m:
#         print(*s)
#         return
#
#     for i in range(1, n + 1):
#         if i in s:
#             continue
#         s.append(i)
#         f()
#         s.pop()
# f()


def solve(d, n, m):
    if d == m:
        print(" ".join(map(str, result)))
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result.append(i + 1)
            solve(d + 1, n, m)
            visited[i] = False
            result.pop()

n, m = map(int, sys.stdin.readline().split())

visited = [False] * n
result = []
solve(0, n, m)