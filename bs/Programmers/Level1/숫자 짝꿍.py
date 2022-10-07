from collections import deque
def solution(X, Y):
    # arr1 = list(map(str,X))
    # arr2 = list(map(str,Y))
    # res = []
    # for i in range(len(arr2)):
    #     for j in arr1:
    #         if j in arr2:
    #             res.append(j)
    #             arr2.remove(j)
    dic = {}
    dic2 = {}
    res = {}
    for i in X:
        dic[i] = 0
    for i in X:
        dic[i] += 1

    for i in Y:
        dic2[i] = 0
    for i in Y:
        dic2[i] += 1

    for key,values in dic.items():
        if key in dic2:
            res[key] = min(values,dic2[key])
    ans = []

    for key,values in res.items():
        for i in range(values):
            ans.append(key)

    if not ans:
        return "-1"
    if all('0' == x for x in ans):
        return "0"
    else:
        return ''.join(i for i in sorted([i for i in ans], reverse=True))

    # if all
    # res = [str(i) for i in sorted([int(i) for i in res], reverse=True)]
    # print(res)
    # return ''.join(res) if res else "-1"
    # return True





# print(solution("12321", "42531"))
# print(solution("100", "2345"))
# print(solution("100", "203045"))
# print(solution("5525", "1255"))
