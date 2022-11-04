def solution(s):
    list = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2+ 1):
        res = ''
        count = 1
        slice = s[:i]
        for j in range(i, len(s)+i, i):
            if slice == s[j:i+j]:
                count += 1
            else:
                if count == 1:
                    res += slice
                else:
                    res += str(count) + slice
                slice = s[j:j+i]
                count = 1
        list.append(len(res))
    return min(list)

print(solution("aabbaccc"))

