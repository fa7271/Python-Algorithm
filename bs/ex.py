import sys
from collections import defaultdict
from itertools import combinations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# # 소영이 반례
# n = 8
# lst = [1,5,5,1,3,8,4,5]
# res = []
# for i in range(1,n+1):
#     for j in combinations(lst,i):
#         print(j)
#         res.append(sum(j))
# print(sorted(res))
# llst = [1, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 28, 28, 28, 29, 30, 31, 31, 32]
# llist = ' '.join(map(str, llst))
#

from itertools import combinations

n = int(input())
lst = list(map(int, input().split()))
dic = defaultdict(int)

for i in lst:
    dic[i] += 1

sum_combi = lst[-1]  # 모든 조합의 함
com = []  # 조합 넣을 거
com_sum = 0  # 조합의 함

def validate(com):
    count_dict = defaultdict(int)
    for num in com:
        count_dict[num] += 1
        if count_dict[num] > dic[num]:
            return False
    return True

def bt(depth, start):
    global com_sum
    if len(com) == n and sum_combi == com_sum:
        if validate(com):
            print(com)
            exit()
        else:
            return
    for i in range(start, len(lst)):
        if len(com) < n and com_sum <= sum_combi:
            com.append(lst[i])
            com_sum += lst[i]
            bt(depth+1, i+1)
            com.pop()
            com_sum -= lst[i]

bt(0, 0)
print(-1)
# 4
# 1 1 2 5 5 6 6 6 6 7 7 10 11 11 12
# 1 5 1 5