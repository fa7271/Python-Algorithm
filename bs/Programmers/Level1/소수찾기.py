def solution(n):

    answer = [0] * (n+1)

    for i in range(2, n+1 ):
        for j in range(2, n+1):
            count = i * j
            if count > n:
                break
            answer[count] = 1
    return answer.count(0) - 2

print(solution(5))