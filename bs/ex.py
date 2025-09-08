import sys
from collections import defaultdict
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# # 소영이 반례
# n = 3
# lst = [1,5,1,5]
# res = []
# for i in range(1, n + 1):
#     print(i)
#     for j in combinations(lst, i):
#         res.append(sum(j))
# print(sorted(res))
# llst = [1, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 28, 28, 28, 29, 30, 31, 31, 32]
# llist = ' '.join(map(str, llst))
#
#
from itertools import combinations
from collections import defaultdict

n = int(input())
lst = list(map(int, input().split()))
dic = defaultdict(int)

for i in lst:
    dic[i] += 1

target_sum = lst[-1]  # 목표 합
com = []  # 조합을 담을 리스트
com_sum = 0  # 현재 조합의 합

def backtrack(depth, start):
    global com_sum
    # n개의 조합을 뽑았고, n개의 합이 Com 마지막 값과 같음
    if len(com) == n and com_sum == target_sum:
        # 리스트 출력
        print(*com)
        exit()

    for i in range(start, len(lst)):
        if len(com) < n and com_sum <= target_sum and dic[lst[i]] > 0:
            com.append(lst[i])
            com_sum += lst[i]
            dic[lst[i]] -= 1

            # 백트래킹을 사용하여 조건을 만족하는 경우에만 재귀 호출
            backtrack(depth + 1, i)

            com.pop()
            com_sum -= lst[i]
            dic[lst[i]] += 1

backtrack(0, 0)
print(-1)
# 4
# 1 1 2 5 5 6 6 6 6 7 7 10 11 11 12
# 1 5 1 5
# 1515
# 151 515
# 15 11 15 /51 55 15
# 1 5 1 1 1 5 5 1 5 5 1 5