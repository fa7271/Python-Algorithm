import sys
# from collections import deque
#
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
#
# N = int(input())
# lst = deque([int(sys.stdin.readline()) for i in range(N)])
#
# count = 0
# stk = deque()
# left = 0
# right = 0
# while left < N and right < N:
#     if len(stk) <= 1: # 길이가 2 미만 이면
#         stk.append(lst[right])
#         right += 1
#     else:
#         if stk[-1] <= lst[left] and stk[-1] <= lst[right-1] : # 길이가 2 이상 이면서, 사잇 값 이면 추가됨
#             stk.append(lst[right])
#             right += 1
#             count += 1
#         else: # 사잇값이 아님
#             stk.popleft()
#             left += 1
# print(count + N-1 )

n = int(input())
stack = []
res = 0

for _ in range(n):
    now = int(input())
    count = 1
    while stack and stack[-1][0] <= now:
        if stack[-1][0] == now :
            res += stack[-1][1]
            count = stack[-1][1] + 1
            stack.pop()
        else:
            res += stack[-1][1]
            stack.pop()
    if stack: #
        res += 1
    stack.append((now,count))
print(res)




