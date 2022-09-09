def solution(n):
    x = 2
    while x < n:
        if n % x == 1:
            return x
        else: x += 1





print(solution(12))