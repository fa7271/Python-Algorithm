def solution(N, stages):

    result = {}
    length = len(stages)

    for i in range(1, N + 1):
        if length != 0:
            count = stages.count(i) # 분자
            result[i] = count / length
            length -= count # 분모 갯수
        else: result[i] =0
    return sorted(result , key=lambda x:result[x] ,reverse=True)


print(solution(4, [4,4,4,4,4]))