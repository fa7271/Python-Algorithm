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

n, m = map(int, sys.stdin.readline().split())


def solve(num):
    if num == m:
        print(" ".join(map(str, result)))
        return
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result.append(i + 1)
            solve(num+1)
            visited[i] = False
            result.pop()


visited = [False] * n
result = []
solve(0)