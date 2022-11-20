import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


n,m = map(int,input().split())
x =sorted(list(map(int,input().split())))

result = []


def bt():
    if len(result) == m:
        print(*result)
        return
    number = 0
    for i in range(n):
        if number != x[i]:
            result.append(x[i])
            number = x[i]
            bt()
            result.pop()

bt()
