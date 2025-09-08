def solution(s):
    res =[]
    for i in range(0,len(s)):
        if s[i] not in s[:i]:
            res.append(-1)
        else:
            str = s[:i][::-1]
            res.append(str.find(s[i]) + 1)
    return res
print(solution("banana"))
print(solution("foobar"))
