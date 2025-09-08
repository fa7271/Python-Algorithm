def solution(n):
    # x = 2
    # while x < n:
    #     if n % x == 1:
    #         return x
    #     else: x += 1
    return [i for i in range(1,n+1) if n % i == 1][0]





print(solution(12))