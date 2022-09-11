def solution(n):
    answer = ''

    while n >= 1:
        n, remainder = divmod(n, 3)
        answer += str(remainder)

    answer = int(answer,3)
    return answer


print(solution(45))
