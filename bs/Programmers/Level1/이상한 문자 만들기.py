def solution(s):
        return ' '.join([''.join( [b.upper() if a % 2 == 0 else b.lower() for a, b in enumerate(i)] ) for i in s.split(' ')])
print(solution("try hello world"))