def valid_result(base, expression):
    # expression의 결과를 계산하여 반환하는 함수
    if '+' in expression:
        a, b = expression.split(' + ')
        return (int(a, base) + int(b, base))
    elif '-' in expression:
        a, b = expression.split(' - ')
        return (int(a, base) - int(b, base))

def solution(expressions):
    results = []

    for expression in expressions:
            # 지워진 값이 있는 수식 처리
            left, right = expression.split(' = ')
            print(left,right)
            found = set()  # 가능한 결과를 저장할 집합

            # 2진법부터 9진법까지 검토
            for base in range(2, 10):
                try:
                    calculated = valid_result(base, left)
                    if 0 <= calculated < base:  # 결과가 진법의 범위 안에 있어야 함
                        found.add(calculated)
                except ValueError:
                    continue
            print(found)
            if len(found) == 0:
                results.append(expression)  # 결과를 찾을 수 없는 경우
            elif len(found) == 1:
                results.append(f"{left} = {found.pop()}")  # 유일한 결과가 있는 경우
            else:
                results.append(f"{left} = ?")  # 결과가 여러 개인 경우
        # results.append(expression)

    return results


print(solution(["51 - 5 = 44"]))
# print(solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]))
# print(solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]))
# print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]))
# print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]))
