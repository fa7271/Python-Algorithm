def solution(s):

    return s.isnumeric() if len(s)== 4 or len(s) == 6 else False
print(solution("234"))
