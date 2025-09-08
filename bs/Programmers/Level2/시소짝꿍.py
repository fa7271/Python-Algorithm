from itertools import combinations, product


def solution(weights):
    count = 0
    lists = tuple(combinations(weights,2))
    times = tuple(product([2,3,4],repeat = 2))
    # for list in lists:
    #     for time in times:
    #         if list[0] == list[1]:
    #             count += 1
    #             break
    #         if list[0] * time[0] == list[1] * time[1]:
    #             count += 1
    #             break
    # return count

#     시간 초과 코드
# print(solution([100,180,360,100,270]))


from collections import defaultdict

def solution1(weights):
    answer = 0
    dict1 = defaultdict(int)
    w_dict = defaultdict(int)
    for i in weights:
        tmp = dict1[i*2] + dict1[i*3] + dict1[i*4]
        if tmp != 0 and i in w_dict:
            tmp -= 2 * w_dict[i]
        for j in range(2,5):
            dict1[i*j] += 1
        w_dict[i] += 1
        answer += tmp
    return answer
# print(solution1([100,180,360,100,270]))

def solution2(weights):
    dic={}
    ratios = [4/2, 4/3, 3/2, 2/3, 3/4, 2/4]
    answer = 0
    for weight in weights:
        if weight in dic:
            dic[weight]+=1
        else:
            dic[weight]=1
    for w in weights:
        for ratio in ratios:
            if int(w*ratio) != w*ratio :
                continue
            if int(w*ratio) in dic :
                answer += dic[int(w*ratio)]
        answer += (dic[w] - 1)
    return answer//2
print(solution2([100,180,100,360]))
# print(solution2([100,180,360,100,270]))
# iterate over each person and ratio

def solution3(weights):
    # arr[w] = # of people of weight w
    arr, res = [0] * 2001, 0
    # possible ratios
    ratio = [4/2, 4/3, 3/2, 2/3, 3/4, 2/4]

    # update data
    for w in weights:
        arr[w] += 1
    # iterate over each person and ratio
    for w in weights:
        for r in ratio:
            # invalid index
            if int(w*r) != w*r: continue
            # add number of pairable people
            res += arr[int(w*r)]

        # people with same weight except me
        res += (arr[w]-1)

    # pair (A, B) == (B, A)
    return res // 2
# print(solution3([100,180,360,100,270]))
