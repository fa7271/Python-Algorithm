from collections import defaultdict
from itertools import combinations

import numpy as np


def solution(friends, gifts):
    dic = {f: i for i, f in enumerate(friends)}  # 인덱스 저장
    graph = [[0] * len(friends) for _ in range(len(friends))]  # 선물 준 리스트
    presents = [0] * len(friends)

    # 선물 준거 그래프 형
    for gift in gifts:
        x, y = gift.split(" ")
        graph[dic[x]][dic[y]] += 1
    give = [sum(i) for i in graph]
    take = []
    for x in range(len(friends)):
        res = 0
        for y in range(len(friends)):
            res += graph[y][x]
        take.append(res)

    jisu = [give[i] - take[i] for i in range(len(friends))]
    for x in range(len(friends)):
        for y in range(x+1,len(friends)):
            if graph[x][y] > graph[y][x]: # x가 준게 더 많음
                presents[x] += 1
            elif graph[y][x] > graph[x][y] : # y가 더 많음
                presents[y] += 1
            else: # 같거나 기록이 없음
                if jisu[x] > jisu[y]:
                    presents[x] +=1
                elif jisu[y] > jisu[x]:
                    presents[y] += 1
    return max(presents)




print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
