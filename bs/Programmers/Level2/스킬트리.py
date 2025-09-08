from collections import deque

def solution(skill, skill_trees):
    # pre_skill = skill[:-1]
    # count = 0
    # for i in skill_trees:
    #     if pre_skill in i :
    #         count += 1
    # print(count)
    # while
    pre_skill = skill[:-1]
    skill_trees =deque(skill_trees)
    print(skill)
    count = 0

def solution(skill, skill_trees):
    res = 0
    for tree in skill_trees:
        str = ''
        for i in tree:
            print(i)
            if i in skill:  # 선행스킬에 포함된다면
                str += i
        if skill[:len(str)] == str:  # skill의 앞부터 s의 길이만큼 s와 같다면
            res += 1  # 가능
    return res


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))