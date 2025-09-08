def solution(N, number):
    if number == N:
        return 1

    list =[set() for i in range(8)] # 최솟값이 8 이기 때문

    for i in range(len(list)):
        list[i].add(int(str(N)*(i+1)))

    for i in range(1,8):
        for j in range(i):
            for op1 in list[j]:
                for op2 in list[i-j-1]:
                    list[i].add(op1+op2)
                    list[i].add(op1-op2)
                    list[i].add(op1*op2)
                    if op2 != 0:
                        list[i].add(op1//op2)
        if number in list[i]:
            answer = i+1
            break
    else:
        answer = -1
    return answer

print(solution(5,12))

def solution(N, number):
    dp = [[]]

    x = 0
    for i in range(1, 9):
        dp.append(set())
        x = 10*x + N
        dp[i].add(x) # N, NN, NNN...

        for j in range(i):
            # 연산자 케이스
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)


            if number in dp[i]:
                return i

    return -1