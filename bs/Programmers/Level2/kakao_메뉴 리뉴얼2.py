from itertools import combinations
def solution(orders, course):
    ans = []
    foodmap = [{} for _ in range(11)]
    maxCnt = [0 for _ in range(11)]
    for str in orders:
        for num in range(2, len(str) + 1):
            for i in combinations(sorted(str), num):
                key = ''.join(i)
                if key in foodmap[num]:
                    foodmap[num][key] += 1
                    maxCnt[num] = max(maxCnt[num], foodmap[num][key]) # 맥스값 업데이트
                else:
                    foodmap[num][key] = 1
                    break
    for num in course:
        for key, value in foodmap[num].items():
            if value >= 2 and value == maxCnt[num]:
                ans.append(key)
    print(ans)
    print(maxCnt)
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))