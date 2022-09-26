def solution(n, left, right):
    # list = [i for i in range(1,n+1)]
    # # print(list[0])
    # res = []
    # for i in range(n):
    #     if i == 0:
    #         res.append(list)
    #     elif i > 0:
    #         res.append([i+1]*(i+1)+list[i+1:])
    # res = sum(res, [])
    # return(res[left:right+1])
    answer = []
    for i in range(left,right+1):
        x = i // n # 몫
        y = i % n #나머지
        print(x,y)

        answer.append(max(x,y)+1)

    return answer
print(solution(4,7,14))
# (0,0)
# (0,1),(1,0)(1,1)
# (0,2),(1,2),(2,0),(2,1),(2,2)
