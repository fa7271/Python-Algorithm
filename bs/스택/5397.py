import sys

sys.stdin = open('/Python/h.txt', 'r')

t = int(input())

for i in range(t):
    arr = list(map(str, input()))
    left = []
    right = []
    for word in arr:
        if word == "<":
            if left:
                right.append(left.pop())
        elif word == ">":
            if right:
                left.append(right.pop())
        elif word == "-":
            if left:
                left.pop()
        else:
            left.append(word)
    left.extend(reversed(right))
    print("".join(left))