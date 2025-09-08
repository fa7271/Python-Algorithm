import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
expression = list(input())
dict = {chr(65 + i): int(input()) for i in range(n)}

stack = []

for ex in expression:
    if ex in ["*", "/", "-", "+"]:
        right = stack.pop()
        left = stack.pop()
        if ex == '+':
            stack.append(left + right)
        elif ex == '-':
            stack.append(left - right)
        elif ex == '*':
            stack.append(left * right)
        elif ex == '/':
            stack.append(left / right)
    else:
        stack.append(dict[ex])
print('%.2f' %stack[0])
