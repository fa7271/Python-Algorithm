import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
stk = []
for _ in range(n):
    x = sys.stdin.readline().rstrip()
    if x[0] == str(1):
        stk.append(int(x.split(" ")[1]))
    elif x[0] == str(2):
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif x[0] == str(3):
        print(len(stk))
    elif x[0] == str(4):
        if len(stk) != 0:
            print(0)
        else:
            print(1)
    elif x[0] == str(5):
        if stk:
            print(stk[-1])
        else:
            print(-1)

