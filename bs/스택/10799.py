import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

x = list(map(str, sys.stdin.readline().rstrip()))
stack = []
res = 0
for idx, i in enumerate(x):
    if i == "(":
        stack.append("(")
    else:
        if x[idx - 1] == "(":
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res += 1
print(res)
