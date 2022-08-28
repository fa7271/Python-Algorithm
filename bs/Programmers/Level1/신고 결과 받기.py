def solution(id_list, report, k):
    answer = []
    #{} 키가 신고한사람 밸류가 당한사람
    arr = {} #  키가 신고당한아이디 밸류가 신고한아이디 set
    answerDic = {}
    for i in range(len(id_list)):
        arr[id_list[i]] = set()
        answerDic[id_list[i]] = 0

    # print(answerDic) {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}
    # print(answerDic)
    for i in range(len(report)):
        reporter, reported = report[i].split(" ")
        arr[reported].add(reporter)
    print(arr)

    res = []
    for name, v in arr.items():
        res.append(len(arr.get(name)))
    print(res)

    result = {}
    for i in range(len(res)):
        result[id_list[i]] = res[i]

    print(result)

    value = list(result.keys())

    sol = {}
    for i in range(len(id_list)):
        sol[id_list[i]] = 0

    # print(sol)
    x = []
    for i in range(len(result)):
        if(result.get(value[i]) >= k):
            print(arr[value[i]])

            x.append((arr[value[i]]))

    print("----------")
    print(x[0])
    print(x[1])

    # for value in result.values():
    #     list.append(value, end=',')
    #     print(list)



    # print(result)
    # for id, rpt  in arr.items:
    #     reporter, reported = report[i].split(" ")
    #     # if id in succ:
    #     #     for i in range(len(list(rpt.values())))
    #
    #     for j in range(len(succ)):
    #         if(rpt):
    #             answerDic[reporter] += 1
    #
    # answer = list(answerDic.values())

    #1. 신고 처리된 사람(k번 이상 신고 받은 사람)
    #1-1 신고 횟수 계산
    #   키가 신고당한 아이디 밸류가 신고한아이디 set
    #   set에 신고한 id 넣기
    #   set의 요소 갯수를 세면 신고 받은 횟수 확인 가능
    #2. 처리된 신고를 한 사람
    # cur_price['naver'] = 800000

    return answer

solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)
# solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)

# 1. 한 사람당 한 명을 신고할 수 있다.
# 1-1 한 사람 똑같은 사람을 신고 할 수 없다 >> 신고 당한사람이 중복하여 들어오면 set 으로 한개로 만들어줌
# 1-2 키는 신고당한 아이디 / 벨류는 신고한 사람의 아이디
#
# 2. 신고 당한 사람이(report) 의 총 카운트가 k 보다 높으면 신고 한 사람들 의 카운트가 올라간다.
# arr의 딕셔너리를 돌면서


