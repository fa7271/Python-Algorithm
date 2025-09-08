

def solution(cards):

    res = []
    for i in range(len(cards)):
        left = 0
        while cards[i] != 0:
             next = cards[i] -1
             cards[i], i = 0, next
             left += 1
        res.append(left)
    res.sort()
    return res[-1] * res[-2]
print(solution([8,6,3,7,2,5,1,4]))


