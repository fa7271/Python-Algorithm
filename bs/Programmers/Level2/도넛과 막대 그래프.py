from collections import defaultdict


def solution(edges):
    res = [0, 0, 0, 0]
    dic = defaultdict(lambda: [0, 0])

    for x, y in edges:
        # 준거
        dic[x][0] += 1
        # 받은거
        dic[y][1] += 1
    for node, item in dic.items():
        give = item[0]
        take = item[1]
        # 기준 노드찾기, 들어오는건 없고 나가는게 2개 이상임
        if give >= 2 and take == 0:
            res[0] = node
        # 8자형 :8자형 시작 노드는 나가는거 들어오는거 2개 이상임
        elif give >= 2 and take >= 2:
            res[3] += 1
        # 막대기형: 마지막 도착 노드가 받기만 함 주는건 없음
        elif give == 0 and take >= 1:
            res[2] += 1
    x = dic[res[0]][0]
    res[1] = x - res[2] - res[3]
    return res
# print(solution([[2, 3], [4, 3], [1, 1], [2, 1]])) # [2, 1, 1, 0]
print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3],[11, 9], [3, 8]]))  # [4,0,1,2]

# 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수
