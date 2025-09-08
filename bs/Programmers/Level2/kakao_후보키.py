from itertools import combinations

def solution(relation):
    row = len(relation) # 행
    col = len(relation[0]) # 열

    #가능한 속성의 모든 인덱스 조합
    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))

    arr = set()
    res = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        if row == len(set(tmp)): # 겹치는게 없으니 열이 같다 >> 중복된 값이 없음 # 유일성
            arr.add(i)
            # 유일성 통과하면 희소성
            flag = True
            for j in res:
                if set(j).issubset(set(i)): # 겹치는게 있으면
                    flag = False
            if flag: # 맨 처음 빈 리스트일때 넣음 / 희소성일때 넣음
                res.append(i)
    return len(res)



        # if set(i).issubset(arr):
        #     print('s')


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))