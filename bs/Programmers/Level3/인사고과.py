def solution(scores):
    a,b = scores[0],scores[1]
    dic = dict()
    scores.sort(key=lambda x: (-x[0], x[1]))
    for x,y in scores:
        if (x+y) not in dic:
            dic[x+y] = 1
        else:
            dic[x+y] += 1
    x = sorted(dic.items(),reverse=True)


# print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))

def solution2(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)
    scores.sort(key=lambda s: (-s[0], s[1])) # 근무 / 동기
    max_company, answer = 0, 1 # 이미 근무로 내림차순하고 동기로 오름차순이므로 근무점수는 비교하지않아도 되므로 동기점수를 저장한다.
    for s in scores:
        if wanho[0] < s[0] and wanho[1] < s[1]:
            return -1
        if max_company <= s[1]:
            if wanho_sum < s[0] + s[1]:
                answer += 1
            max_company = s[1]
    return answer
print(solution2([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))
