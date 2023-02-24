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
        res = 0
        for t in target:
            if t not in value:
                res = -1
                break
            res += value[t]
        ans.append(res)
    return ans

print(solution(	["ABACD", "BCEFD"], ["ABCD", "AABB"])) # [9,4]
print(solution(	["AA"], ["B"])) # [-`]
print(solution(	["AGZ", "BSSS"], ["ASA", "BGZ"])) #[4,6]