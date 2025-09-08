import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
N =int(sys.stdin.readline())

lst = [False, False] + [True] * (N-1)
res = []
for i in range(2, N+1):
    if lst[i]:
        res.append(i)
        for j in range(2*i, N+1, i):
            lst[j] = False
res.append(0)
left, right = 0, 0
result = res[0]
count = 0
while right < len(res)-1:
    if result == N:
        count += 1
        result -= res[left]
        left += 1
        right += 1
        result += res[right]
    elif result < N:
        right += 1
        result += res[right]
    else:
        result -= res[left]
        left += 1
print(count)






