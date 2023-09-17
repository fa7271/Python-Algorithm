
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
str_lst = list(sys.stdin.readline().rstrip() for _ in range(n))
count = 0
for i in str_lst:
    stk = []
    for s in i:
        stk.append(s)
        if len(stk) >= 2 and stk[-1] == stk[-2] :
            stk.pop()
            stk.pop()
    if not stk:
        count += 1
print(count)
