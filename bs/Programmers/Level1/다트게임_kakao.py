def solution(dartResult):

    point = ['10' if i =='A' else i for i in dartResult.replace('10', 'A')] # 다시 A 이면 10으로 해서 저장

    dic = {"S" : 1,
           "D" : 2,
           "T" : 3}

    stack = []

    for i in point:
        print(stack)
        if i.isnumeric() or i =="A":
            stack.append(10 if i =="A" else int(i))
        elif i in["S", "D", "T"]:
            now = stack.pop()
            stack.append(now ** dic[i] )
        elif i =="#":
            stack[-1] *= -1
        elif i == "*":
            now = stack.pop()
            print(now)
            if len(stack):
                stack[-1] *= 2
            stack.append(2 * now)

    return sum(stack)





print(solution("1S*2T*3S"))