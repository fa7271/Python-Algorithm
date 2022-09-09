def solution(num):
    count = 0
    if num == 1:
        return 0

    while True:
        num = num / 2 if num % 2 == 0 else( num * 3 ) + 1
        count += 1
        if num ==1:
            return count
        elif count == 500:
            return -1

print(solution(6))