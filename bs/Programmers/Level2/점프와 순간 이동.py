def solution(n):
    count = 0
    while n > 0:
        if n%2 == 1:
            n -= 1
            count += 1
        else:
            n /= 2
    return count

print(solution())