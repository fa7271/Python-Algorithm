

def solution1(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0
    print(deliveries,pickups)
    d = 0
    p = 0

    for i in range(n):
        d += deliveries[i]
        p += pickups[i]
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            print(n-i)
            answer += (n - i) * 2
    return answer

# print(solution1(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))


def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups:
        while deliveries and deliveries[-1] == 0:
            del deliveries[-1]
        while pickups and pickups[-1] == 0:
            del pickups[-1]
        answer += 2 *(max(len(deliveries),len(pickups)))
        x = cap
        for i in reversed(range(len(deliveries))):
            if x < deliveries[i]: # 더 많이 가지고 있음
                deliveries[i] -= x
                break
            else:
                x -= deliveries[i]
                deliveries[i] = 0
        y = cap
        for i in reversed(range(len(pickups))):
            if y < pickups[i]: # 더 많이 가지고 있음
                pickups[i] -= y
                break
            else:
                y -= pickups[i]
                pickups[i] = 0
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
