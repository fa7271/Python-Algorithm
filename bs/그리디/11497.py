import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(input())
for i in range(t):
    n = int(input())
    numbers = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
    _left, _right = [],[]
    idx = 1
    for i in numbers:
        if idx%2:
            _left.append(i)
        else:
            _right.append(i)
        idx +=1
    _right.reverse()
    _left.extend(_right)
    res = [abs(_left[i+1]-_left[i]) for i in range(len(_left)-1)]
    print(max(res))
