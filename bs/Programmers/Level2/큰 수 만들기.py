# from collections import deque
# def solution(number, k):
#     num = deque(number)
#     count = k
#     list = [0] * k
#     while count > 0:
#         now = num.popleft()
#         if any(now < i for i in num) and :
#             count -= 1
#             list.append(now)
#         else :
#     print(list)
# print(solution("4177252841",4))

def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)
print(solution("4177252841",4))
