def solution(n):
    # x = sum([int(i) for i in str(n)])
    # return n % x == 0

    return n % sum([int(i) for i in str(n)]) == 0

print(solution(11))