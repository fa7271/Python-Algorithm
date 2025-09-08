import sys
from collections import deque
from itertools import combinations


def solution(levels, k):
    levels.sort(reverse=True)  # 내림차순으로 정렬
    max_levels = levels[0]
    max_count = 1
    mk = k
    levels.pop(0)
    for i in levels:
        if max_levels - i <= mk:
            mk -= i
            max_count += 1
        else:
            break
    # max_count 최댓값의 갯수
    res = set()
    def bt(depth, temp_res, k):
        if depth == max_count:
            for i in temp_res:
                res.add(i)
        for i in levels:
            diff = max_levels - i
            if k >= diff:
                k -= diff
                temp_res.append(i)
                bt(depth + 1, temp_res, k)
                temp_res.pop()
                k += diff
    bt(1, [], k)
    return len(set(levels)) - len(res)
print(solution([7, 1, 2, 4, 3], 8)) # 1
print(solution([100, 99, 1, 1], 99))  # 0

# 7 4 3 2 1
# 7 4+4 2+5
