import math
def solution(n):

    dic = {i:0 for i in n.lower()}
    for i in n.lower():
        dic[i] += 1
    return "true" if dic.get('p') == dic.get('y') else "false"

print(solution("pPoooyY"))
# return "Even" if num % 2 ==0 else "Odd"

# #for i in set(report):
# reported[i.split()[1]] += 1
# print(reported)