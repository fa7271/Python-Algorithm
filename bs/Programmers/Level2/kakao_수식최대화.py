import re
import itertools
def solution(expression):
    operators = list(itertools.permutations( ['-','+','*'],3))
    expression = re.split('([-|+|*])', expression)
    res = []
    for operator in operators:
        exp = expression[:]
        for op in operator:
            while op in exp: # 똑같은 연산자가 여러개일수도 있음
                idx = exp.index(op)
                exp[idx-1] = str(eval(exp[idx-1] + op + exp[idx+1])) # 연산 기준 앞뒤로 반환
                del exp[idx: idx+2] # 맨 앞에 넣고 두개 삭제
        res.append(abs(int(exp[0])))
    return max(res)
print(solution("100-200*300-500+20"))
# 1. 숫자와 문자열 분리