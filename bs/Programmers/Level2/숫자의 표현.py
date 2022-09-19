def solution(s):
    res = 0
    s = int(s)
    for i in range(1, s+1):
        count = 0
        for j in range(i, s+1):
            count += j
            if count == s:
                res += 1
                break
            elif count > s:
                break
    return res

print(solution("15"))