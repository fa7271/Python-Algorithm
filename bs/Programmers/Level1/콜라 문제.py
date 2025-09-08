

def solution(a, b, n):
    count = 0
    while True:
        count += n // a * b
        n = n // a * b + (n % a)
        if n//a == 0: break
    return count

print(solution( 3, 1, 20))
