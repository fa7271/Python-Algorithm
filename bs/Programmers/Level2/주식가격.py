from collections import deque
def solution(prices):
    res = []
    while prices:
        count = 0
        now = prices.pop(0)
        for i in prices:
            count += 1
            if now > i:
                break
        res.append(count)
    return res


    queue = deque(prices)
    res = []
    while queue:
        price = queue.popleft()
        count = 0
        for q in queue:
            count += 1
            if price > q:
                break
        res.append(count)
    return res
print(solution(	[1, 2, 3, 2, 3]))

