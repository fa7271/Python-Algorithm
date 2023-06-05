import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

K = int(input())

# for i in range(K):
#     stk = []
#     str = list(input())
#     for j in str:
#         if j == "(":
#             stk.append(j)
#         elif len(stk) != 0 and stk[-1] == "(":
#             stk.pop()
#         else:
#             stk.append(j)
#     if len(stk) == 0:
#         print("YES")
#     else:
#         print("NO")

for i in range(K):
    line = sys.stdin.readline().rstrip()

    while "()" in line:
        line = line.replace("()","")

    if line:
        print("NO")
    else:
        print("YES")

