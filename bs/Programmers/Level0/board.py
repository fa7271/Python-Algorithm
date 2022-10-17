from itertools import combinations
import re


def solution(id_pw, db):
    for i in db:
        # id 여부 확인
        if id_pw[0] in i:
            if id_pw[1] == i[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"
# print(solution(["p", "o", "s"],["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
# print(solution("apple","elppa"))
# print(solution(	1, 13, 1))
