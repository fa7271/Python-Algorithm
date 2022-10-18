from itertools import combinations, permutations


def solution(score):
    score_list = [sum(i) for i in score]
    list = sorted([sum(i) for i in score], reverse=True)
    print(list)
    print(score_list)
    res = [list.index(i) +1 for i in score_list]

    return res
print(solution(	[[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
# print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))



