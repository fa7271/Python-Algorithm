def solution(name):
    mini = len(name) -1
    res = 0
    for i, char in enumerate(name):
        res += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        mini = min([mini, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
    res += mini

    return res

print(solution("JEROEN"))

