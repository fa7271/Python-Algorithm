from collections import deque


# 너무 dp 같은데.
# 첫번째 뜯었을경우, 안 뜯었을 경우.
def solution(sticker):
    # 시도 1
    # answer = []
    # for j in range(2):
    #     temp = 0
    #     for i in sticker[j::2]:
    #         temp += i
    #     answer.append(temp)
    # return max(answer)

    # 시도2.
    if len(sticker) <= 2:
        return max(sticker)

    dp = [0] * len(sticker)
    no_dp = [0] * len(sticker)

    dp[0] = sticker[0]
    dp[1] = dp[0]

    # 맨 앞 스티커 뜯은 경우 >> 끝에꺼는 못 뜯음 -> dp[-2] 최대
    for i in range(2, len(sticker) - 1):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])

    # 맨 앞 스티커 안 뜯은경우 > 끝에꺼 뜯음 > no_dp[-1]
    for i in range(1, len(sticker)):
        no_dp[i] = max(no_dp[i - 2] + sticker[i], no_dp[i - 1])
    return max(no_dp[-1], dp[-2])


# print(solution([14, 6, 5, 11, 3, 9, 2, 10]	)) #  36
print(solution([1, 3, 2, 5, 4]))  # 8

# sticker = 1~100,000
