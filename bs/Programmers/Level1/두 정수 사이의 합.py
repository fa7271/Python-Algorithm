def solution(a,b):

    return sum([i for i in range(min(a, b), max(a,b)+1 )])
print(solution(5,3))