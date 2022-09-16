def solution(survey, choices):
    answer =''
    choice = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0, }
    for i in range(len(choices)):
        L = survey[i][0]
        R = survey[i][1]
        if choices[i] == 4:
            continue
        elif choices[i] < 4:
            choice[L] += (4-choices[i])
        else:
            choice[R] += (choices[i] -4)
    answer += 'R' if choice['R'] >= choice['T'] else 'T'
    answer += 'C' if choice['C'] >= choice['F'] else 'F'
    answer += 'J' if choice['J'] >= choice['M'] else 'M'
    answer += 'A' if choice['A'] >= choice['N'] else 'N'
    return answer

print(solution( ["TR", "RT", "TR"], [7,1,3] ))

