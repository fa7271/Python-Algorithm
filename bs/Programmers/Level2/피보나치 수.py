def solution(x):

    fibo = [0, 1]
    for i in range(x-1):
        fibo.append(fibo[i] + fibo[i+1])
    return fibo[x] % 1234567

print(solution(5))

