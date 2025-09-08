import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
lst = list(map(int,sys.stdin.readline().split()))
stk = []
idx = 1
while lst:
    if idx == lst[0]:
        idx += 1
        lst.pop(0)
    else:
        stk.append(lst.pop(0))

    while stk :
        if stk[-1] == idx:
            stk.pop()
            idx +=1
        else:
            break
if stk:print("Sad")
else:print("Nice")