import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())


def dfs(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]

    temp = dfs(n // 2)
    arr = []
    for i in temp:
        arr.append(' ' * (n // 2) + i + ' ' * (n // 2))
    for i in temp:
        arr.append(i + " " + i)
    return arr


print('\n'.join(dfs(n)))
