from functools import reduce
def solution(clothes):
    dic = {y : 0 for x, y in clothes}
    for i in clothes:
        dic[i[1]] += 1
    print(dic.values())

    return reduce(lambda x,y: x*y,[i+1 for i in dic.values()]) - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
