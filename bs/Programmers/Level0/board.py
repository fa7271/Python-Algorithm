def solution(cipher, code):
    res =[]
    i = code - 1
    while i < len(cipher):
        res.append(cipher[i])
        i += code
    return "".join(res)

    answer = cipher[code-1::code]
print(solution("dfjardstddetckdaccccdegk",4))
