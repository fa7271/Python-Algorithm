
# def solution(s):
    # list = [i for i in s]
    # list.append(list[0])
    # count = 0
    # if len(list) == 0: return 0
    # for left, right in zip(list,list[1:]):
    #     print(left,right)
    #     if left == '[' and right == ']':
    #         count += 1
    #     elif left == '(' and right == ')':
    #         count += 1
    #     elif left == '{' and right == '}':
    #         count += 1
    #     # elif left == ']' or '}' or ')' :
    #     #     pass
    # return count
from collections import deque

def isCorrect(s):
        stack = []
        s = deque(s)

        while s:
            tmp = s.popleft()
            if stack:
                if tmp == ']' and stack[-1] == '[':
                    stack.pop()
                elif tmp == '}' and stack[-1] == '{':
                    stack.pop()
                elif tmp == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(tmp)
            else:
                stack.append(tmp)

        return True if not stack else False

def solution(s):
    answer = 0

    for i in range(len(s)):
        if isCorrect(s[i:] + s[:i]):
            answer += 1

    return answer
print(solution("[](){}"))
