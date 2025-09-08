import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

S = set()
T = int(sys.stdin.readline())

for i in range(T):
    order = sys.stdin.readline().split()
    if len(order) == 1:
        if order[0] == 'all':
            S = set([x for x in range(1, 21)])
        else:
            S = set()
    else:
        cmd, x = order[0], int(order[1])
        if cmd == 'add':
            S.add(x)
        elif cmd == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif cmd == 'remove':
            if x in S:
                S.discard(x)
        elif cmd == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
