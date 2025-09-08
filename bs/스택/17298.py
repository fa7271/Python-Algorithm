import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline().rstrip())
Numbers = list(map(int,sys.stdin.readline().split(" ")))


stk = []  #
res = [-1] * N  # 오큰수를 저장할 리스트

for i in range(N):
    while stk and Numbers[stk[-1]] < Numbers[i]:
        idx = stk.pop()
        res[idx] = Numbers[i]
    stk.append(i)

print(*res)
