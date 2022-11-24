def solution(k, tangerine):
    dic = {x:0 for x in set(tangerine)}
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else: dic[i] = 0

    list = sorted(dic.items(),key=lambda x : x[1],reverse=True)
    result = [0,0] # / 종류별 귤
    for a, b in list:
        if list[0][1] > k:
            return 1
        result[0] += 1
        result[1] += b
        if result[1] >= k:
            break
    return result[0]

print(solution(	6, [1, 3, 2, 5, 4, 5, 2, 3])) # 3

from collections import Counter

def solution1(k, tangerine):
    c = Counter(tangerine)
    answer = 0

    c = sorted(c.items(), key=lambda x:x[1], reverse=True)
    print(c)

    if c[0][1] > k :
        return 1

    box = 0
    for t,cnt in c:
        answer+=1
        box += cnt
        # print(t,cnt, box)
        if box >= k:
            break

    return answer

# print(solution1(	6, [1, 3, 2, 5, 4, 5, 2, 3])) # 3
