import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
def check(i):
    cnt = 0
    for a in range(n):
        if a < i:
            if n_list[a] != (n_list[i] - (i-a)*k):
                cnt += 1
        elif a > i:
            if n_list[a] != (n_list[i] + (a-i)*k):
                cnt += 1
    return cnt

n,k = map(int,input().split())
n_list = list(map(int,input().split()))
min_cnt = 1001
for i in range(n):
    if n_list[i] > i*k:
        count = check(i)
        min_cnt = min(min_cnt,count)

print(min_cnt)