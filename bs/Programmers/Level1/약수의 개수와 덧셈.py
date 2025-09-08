def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        res = i ** (1/2)
        if int( res ) == res:
            answer -= i
        else:
            answer += i
    return answer