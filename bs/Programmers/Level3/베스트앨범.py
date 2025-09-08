def solution(genres, plays):
    dic = {}
    dic_sum = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic:
            dic[genre] = [(i,play)]
        else:
            dic[genre].append((i,play))

        if genre not in dic_sum:
            dic_sum[genre] = play
        else:
            dic_sum[genre] += play
    res = []
    for x, y in sorted(dic_sum.items(), key=lambda x:x[1], reverse=True): # 장르 별 큰 값으로 정렬
        for a, b in sorted(dic[x], key=lambda x:x[1], reverse=True)[:2]:
            res.append(a)
    return res
print(solution(["classic", "classic", "classic", "pop"], [500, 150, 800, 2500]))
# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
