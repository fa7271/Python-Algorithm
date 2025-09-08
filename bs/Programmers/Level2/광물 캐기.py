def solution(picks, minerals):
    # picks = [i * 5 for i in picks]
    answer = 0

    # # 스톤으로 캤을때 베이스
    # for i in minerals[:5*sum(picks)]:
    #     if i == "diamond":
    #         Stone_Base.append(25)
    #     elif i =="iron" :
    #         Stone_Base.append(5)
    #     else :
    #         Stone_Base.append(1)
    #
    # 5개씩 끊어읽음
    # for i in range(len(Stone_Base)//5+1) :
    #     m_tire.append(Stone_Base[5*i:5*(i+1)])

    Stone_Base = [25 if i == "diamond" else 5 if i == "iron" else 1 for i in minerals[:5*sum(picks)]]
    div_5 = [Stone_Base[5*i:5*(i+1)] for i in range((len(Stone_Base)-1)//5+1)]
    print(div_5)

    div_5 = sorted(div_5 , key = lambda x : sum(x),reverse=True )
    for i in range(len(picks)):
        while ( picks[i] !=0 and len(div_5) !=0 ) :
            if i == 0 :
                answer += len(div_5[0])
            elif i == 1:
                for j in div_5[0]:
                    if j == 1:
                        answer += 1
                    else :
                        answer += j//5
            else:
                answer += sum(div_5[0])
            picks[i] -= 1
            div_5.pop(0)
    return answer

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))