def solution(n):

    return n[len(n)//2 ] if len(n) % 2 == 1 else n[(len(n)//2-1) : (len(n)//2 +1)]

print(solution("abce"))