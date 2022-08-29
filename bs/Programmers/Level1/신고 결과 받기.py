def solution(id_list, report, k):

    answer = [0] * len(id_list)
    reported = {x:0 for x in id_list}

    print(report)
    for i in set(report):
        reported[i.split()[1]] += 1
    print(reported)

    for i in set(report):
        if reported[i.split()[1]] >= k:
            answer[id_list.index(i.split()[0])] += 1

    print(answer)

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


