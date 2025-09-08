import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


lst = list(sys.stdin.readline().rstrip())
stk = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == "L":
        if lst:
            stk.append(lst.pop())
    elif command[0] == "D":
        if stk:
            lst.append(stk.pop())
    elif command[0] == "B":
        if lst:
            lst.pop()
    else:
        lst.append(command[1])
lst.extend(reversed(stk))
print("".join(lst))
