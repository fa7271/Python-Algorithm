def solution(n):

    answer = [0] * (n+1)

    for i in range(2, n+1 ):
        for j in range(2, n+1):
            count = i * j
            if count > n:
                break
            answer[count] = 1
    return answer.count(0) - 2

def solution(n):
    num = set(range(2, n+1))
    print(num)
    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i, n+1,i)) # 2*i 부터 n+1 까지 i 만큼 증가
    print(num)

print(solution(5))