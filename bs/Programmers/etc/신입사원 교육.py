import heapq
def solution(ability, number):
    heapq.heapify(ability)

    count = 0
    while count != number:
        now1 = heapq.heappop(ability)
        now2 = heapq.heappop(ability)
        n_now = now1 + now2
        heapq.heappush(ability,n_now)
        heapq.heappush(ability,n_now)
        count += 1
    return sum(ability)
        