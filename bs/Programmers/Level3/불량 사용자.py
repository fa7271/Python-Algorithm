from itertools import permutations
import re

def solution(user_id, banned_id):
    n = len(banned_id)
    answer = []
    banned_id = [i.replace("*", ".") for i in banned_id] # 정규식에서의 '.'은 어떠한것들과 대응 와일드카드

    for i in permutations(user_id, n):
        flag = True
        lst = list(i)

        for j in range(n):
            if re.match(banned_id[j], lst[j]) and len(lst[j]) == len(banned_id[j]):

                continue
            else:
                flag = False
                break
        if flag:
            if sorted(lst) not in answer:
                answer.append(sorted(lst))
    return len(answer)
# print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))