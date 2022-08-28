def solution(id_list, report, k):
    answer = []
    #{} 키가 신고한사람 밸류가 당한사람
    arr = {} #  키가 신고당한아이디 밸류가 신고한아이디 set
    answerDic = {}
    for i in range(len(id_list)):
        arr[id_list[i]] = set()
        answerDic[id_list[i]] = 0

    for i in range(len(report)):
        reporter, reported = report[i].split(" ")
        arr[reported].add(reporter)

    succ = [];
    for name, v in arr.items():
        if(len(v) >= k):
            succ.append(name)

    for id, rpt  in arr.items:
        reporter, reported = report[i].split(" ")
        # if id in succ:
        #     for i in range(len(list(rpt.values())))

        for j in range(len(succ)):
            if(rpt):
                answerDic[reporter] += 1

    answer = list(answerDic.values())

    #1. 신고 처리된 사람(k번 이상 신고 받은 사람)
    #1-1 신고 횟수 계산
    #   키가 신고당한 아이디 밸류가 신고한아이디 set
    #   set에 신고한 id 넣기
    #   set의 요소 갯수를 세면 신고 받은 횟수 확인 가능
    #2. 처리된 신고를 한 사람
    # cur_price['naver'] = 800000

    return answer

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
//체크