from itertools import permutations


from itertools import permutations
def solution(k, dungeons):
    # 방문할 순서 조합 만들기
    numbers = list(x for x in range(0,len(dungeons)))
    cases = permutations(numbers,len(dungeons))

    results = []
    # 각 조합에 대해
    for case in cases:
        count, now = 0, k
        # 인덱스를 불러와서
        for idx in case:
            # 최소, 소모 피로도
            least, req = dungeons[idx][0], dungeons[idx][1]
            # 최소 피로도 이상 보유 중이라면 처리
            if now >= least:
                now -= req
                count += 1
            else: break
        results.append(count)
    return max(results)
print(solution(80, [[80, 20], [50, 40], [30, 10]]))