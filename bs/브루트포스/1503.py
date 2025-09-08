import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N, S = map(int,input().split())
lst = set([i for i in range(1, 1001)]) -set(list(map(int,input().split())))
ans = 1e9
for a in lst:
    for b in lst:
        for c in lst:
            ans = min(abs(N-a*b*c), ans)
            if N+1 < a*b*c:
                break
print(ans)