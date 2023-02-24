from collections import defaultdict


def solution(keymap, targets):

    ans = []

    value = defaultdict(int)
    for key in keymap:
        for k,v in enumerate(key):
            if not value[v]:
                value[v] = k + 1
            else:
                value[v] = min(value[v], k+1)
    for target in targets:
        flag = True
        count = 0
        for c in target:
            if(c in value):
                count += value[c]
            else:
                flag = False
                break
        if(flag):
            ans.append(count)
        else:
            ans.append(-1)
    return ans

# print(solution(	["ABACD", "BCEFD"], ["ABCD", "AABB"])) # [9,4]
print(solution(	["AA"], ["B"])) # [-`]
# print(solution(	["AGZ", "BSSS"], ["ASA", "BGZ"])) #[4,6]