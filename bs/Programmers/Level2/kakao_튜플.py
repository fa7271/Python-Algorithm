def solution(n):
    answer = []
    n = n[2:-2]
    n = n.split("},{")
    n.sort(key = len)
    for i in n:
        list = i.split(",")
        for j in list:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))

