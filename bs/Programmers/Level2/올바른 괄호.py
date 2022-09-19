
def solution(s):
    stack = []
    if s[0] == ")" :
        return False
    for i in s:
        if i == "(":
            stack.append(i)
        else :
            if stack ==[]:
                return False
            else:
                stack.pop()
    return True if not stack else False
print(solution(")()("))
