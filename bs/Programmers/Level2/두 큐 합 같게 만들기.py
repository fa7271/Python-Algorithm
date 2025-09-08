from itertools import combinations
from collections import deque
def solution(queue1, queue2):
    queue1,queue2 = deque(queue1), deque(queue2)
    count = 0
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    for i in range(max(len(queue1), len(queue2)) * 4):
        if sum_1 < sum_2:
            now = queue2.popleft()
            queue1.append(now)
            sum_1 += now
            sum_2 -= now
            count += 1
        elif sum_1 > sum_2:
            now = queue1.popleft()
            queue2.append(now)
            sum_1 -= now
            sum_2 += now
            count += 1
        else: return count
    return -1
# print(solution(	[3, 2 , 7, 2], [4, 6, 5, 1]))
# print(solution([1, 2, 1, 2],[1, 10, 1, 2]))
# print(solution( [1, 1], [1, 5] ))
print(solution([], [1,2,1,2,10,1,1,2]))
