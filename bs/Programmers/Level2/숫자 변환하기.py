def solution(x, y, n):
    # count = 0
    # if x == n :
    #     return count
    # if x > n :
    #     return -1
    # else: return -1
    count = 0
    while y > x:
        y -= n
        if y <= n:
            break
        else:
        count += 1
        if x*3 == y:
            break
        if x*2 ==y:
            break
    if count == 0:
        return -1
    else: return count
print(solution(	10, 40, 30))
print(solution(	2, 5, 4))
