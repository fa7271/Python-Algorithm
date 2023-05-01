import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())

lst = []
res = []
for i in range(N):
    x = input().split(" ")
    if x[0] == "push":
        lst.append(x[1])
    elif x[0] =="top":
        if len(lst) == 0:
            res.append(-1)
        else:
            top = lst.pop()
            res.append(top)
            lst.append(top)
    elif x[0] == "size":
        now = len(lst)
        res.append(now)
    elif x[0] =="empty":
        if len(lst) == 0:
            res.append(1)
        else:
            res.append(0)
    elif x[0] == 'pop':
        if len(lst) == 0:
            res.append(-1)
        else:
            now = lst.pop()
            res.append(now)
print(*res,sep="\n")





