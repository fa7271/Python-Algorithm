import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

K = int(input())
stk = []

for i in range(K):
    num = int(sys.stdin.readline())
    if num != 0 :
        stk.append(num)
    else:
        if len(stk) != 0:
            stk.pop()
print(sum(stk))