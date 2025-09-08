import math
def solution(r1, r2):
    answer = 0
    for x in range(1,r2+1):
        # x 값을 가져옴
        max_y = math.floor(math.sqrt(r2 ** 2 - x ** 2)) # 큰 반지름 기준
        min_y = 0 if x > r1 else math.ceil(math.sqrt(r1 ** 2 - x ** 2)) # 작은 반지름 기준
        print(x, max_y,min_y)
        answer += max_y- min_y + 1
        print(answer)

    return answer*4



print(solution(2,3))

