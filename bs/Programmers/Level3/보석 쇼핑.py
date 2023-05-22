import copy
from collections import Counter


def solution(gems):
    res = []
    left, right = 0, 0
    dia_len = len(set(gems))
    gem_counts = Counter()  # 각 보석의 등장 횟수를 세는 Counter 객체

    while right < len(gems):
        gem_counts[gems[right]] += 1  # 보석 등장 횟수를 갱신
        if len(gem_counts) == dia_len:  # 모든 보석 종류가 포함된 경우
            while gem_counts[gems[left]] > 1:  # 최소 범위를 찾기 위해 left를 옮기면서 중복 보석을 제거
                gem_counts[gems[left]] -= 1
                left += 1
            res.append([left+1,right+1])

        right += 1
    res.sort(key=lambda x:(x[1]-x[0],x[0]))  # 최소 범위 기준으로 정렬
    return res[0]

def solution2(gems):
    res = []
    left, right = 0, 0
    dia_len = len(set(gems))  # dia 값 0 으로 해둠
    while right <= len(gems):
        if len(set(gems[left:right+1])) == dia_len:
            res.append([left+1,right+1])
            left += 1
        else:
            right += 1
    res.sort(key=lambda x:(x[1]-x[0],x[0]))
    return res[0]







print(solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution2(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution2(	["AA", "AB", "AC", "AA", "AC"]))
# print(solution2(	["XYZ", "XYZ", "XYZ"]))
# print(solution2(	["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

