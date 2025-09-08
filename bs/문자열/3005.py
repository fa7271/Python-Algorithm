import sys

sys.stdin = open('/Python/h.txt', 'r')

N, M = map(int,sys.stdin.readline().split(" "))
lst = [input() for i in range(N)]

res = []

for i in range(N):
    s = lst[i].split("#")

    for j in s:
        if len(j) >= 2:
            res.append(j)

for i in range(M):
    re=''
    for j in range(N):
        re+=lst[j][i]
    b=re.split('#')
    for l in b:
        if len(l)>=2:
            res.append(l)
print(sorted(res)[0])

