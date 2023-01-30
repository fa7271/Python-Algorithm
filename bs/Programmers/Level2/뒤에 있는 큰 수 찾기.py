import heapq
from collections import deque
def solution(numbers):
    # res = []
    # while numbers:
    #     now = numbers.pop(0)
    #     print(now)
    #     heap = []
    #     for i in numbers:
    #         heapq.heappush(heap,-i)
    #     com_now = heapq.heappop(heap) * -1
    #     print(com_now)
    #     if com_now < now:
    #         res.append(-1)
    #     else:
    #         res.append(com_now)
    #     print(res)

    res = []
    numbers = deque(numbers)
    while numbers:
        now = numbers.popleft()
        x = -1
        for i in numbers:
            if i > now: # i > 9
                x = i
                break
        res.append(x)
    # return res
# from collections import deque
# def solution(prices):
#     queue = deque(prices)
#     res = []
#     while queue:
#         price = queue.popleft()
#         count = 0
#         for q in queue:
#             count += 1
#             if price > q:
#                 break
#         res.append(count)
#     return res


def solution2(numbers):
    stack = []
    answer = [0] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    while stack:
        answer[stack.pop()] = -1

    return answer

# i = 0 stack = [0]
# i = 1 stack = [0,1]
# i = 2 stack = [0,2,3] res = [0, 5]
# i = 3 stack = [0,2] res = [0,5,]

# print(solution(	[2, 3, 3, 5]))
# print(solution(	[9, 1, 5, 3, 6, 2]))
print(solution2([9, 1, 5, 3, 6, 2]))
# print(solution2(	[2, 3, 3, 5]))

