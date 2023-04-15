from functools import reduce


def solution(clothes):
    dic = dict()
    for (key, value) in clothes:
        if value in dic:
            dic[value].append(key)
        else:
            dic[value] = [key]
    # dics = {value: [key] if value not in dic else dic[value] for key, value in clothes}
    res = 0
    num = []
    for i in "headgear", "eyewear", "face" :
        if i in dic:
            res += len(dic[i])
            num.append(len(dic[i]))
    if len(num) > 1 :
        res += reduce(lambda x, y: x * y, num)
    #

    a = [1,2,3,4,5]
    print(reduce(lambda x,y : x+y, a))
    for i in range(1, len(a) + 1):
        print(reduce(lambda x, y: x + y, a[:i]))

    dic = {y : 0 for x, y in clothes}
    for i in clothes:
        dic[i[1]] += 1
    res = 0
    res += reduce(lambda x, y : x*y, [i+1 for i in dic.values()]) - 1
    return res




print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))


