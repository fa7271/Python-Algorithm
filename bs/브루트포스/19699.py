import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, M = map(int,sys.stdin.readline().split(" "))
lst = list(map(int,sys.stdin.readline().split(" ")))
def check(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


res = []
ans = []
def bt(num):
    if len(res) == M:
        x = sum(res)
        if check(x):
            ans.append(x)

    for i in range(num,N):
        res.append(lst[i])
        bt(i+1)
        res.pop()
bt(0)
if len(ans) == 0:
    print(-1)
else:
    print(*sorted(list(set(ans))))

