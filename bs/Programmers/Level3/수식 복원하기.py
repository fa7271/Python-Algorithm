# 10진수 값을 base 진법으로 변환하는 함수
def to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n //= base
    return ''.join(digits[::-1])


def valid_result(base, expression):
    # expression을 공백으로 분리
    ls = expression.split(" ")
    a = int(ls[0], base)  # 첫 번째 숫자
    b = int(ls[2], base)  # 두 번째 숫자
    operator = ls[1]  # 연산자
    # 결과 값이 X인 경우 (X 값을 구해야 하는 상황)
    if ls[4] == "X":
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        return to_base(result, base)  # 계산 결과를 base 진법으로 변환하여 반환

    # 결과 값이 주어진 경우 (정답 검증)
    else:
        c = int(ls[4], base)  # 결과 값
        if operator == "+" and a + b == c:
            return base
        elif operator == "-" and a - b == c:
            return base
    return False


def solution(expressions):
    number_stk = []
    calculate_stk = []
    number = ""
    incorrect_expression = []
    correct_expression = []
    # 시작 할 base 값 구하기

    for expression in expressions:
        if "X" in expression:
            incorrect_expression.append(expression)
        else:
            correct_expression.append(expression)
        express, res = expression.replace(" ", "").split("=")

        if res != "X":
            number += res
        for i in express:
            if i == "+" or i == "-":
                calculate_stk.append(i)
            else:
                number_stk.append(i)
                number += i
    number = sorted(number, key=lambda x: -int(x[0]))
    start_base = int(number[0]) + 1

    # 뭐가 될지 찾아야함.
    answer_list = []
    for n in range(start_base, 10):
        temp = 1
        for correct in correct_expression:
            x = valid_result(n, correct)
            if not x:
                temp = 0
        if temp:
            answer_list.append(n)

    answer_list = list(set(answer_list))
    answer = []
    for incorrect_express in incorrect_expression:
        sets = set()
        for possible_base in answer_list:
            sets.add(valid_result(possible_base, incorrect_express))
        temp = str(sets.pop()) if len(sets) == 1 else '?'
        answer.append(incorrect_express[:-1] + temp)
    return answer


print(solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]))
# print(solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]))
# print(solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]))
# print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]))
# print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]))
