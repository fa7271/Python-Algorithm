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
    if len(sticker)<= 2:
        return max(sticker)
    dp = [-1e9] * len(sticker)
    dp[0] = sticker[0]
    dp[1] = sticker[1]
    for i in range(3,len(sticker)):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
# 시도3.


    return max(dp)
# print(solution([14, 6, 5, 11, 3, 9, 2, 10]	)) #  36
print(solution([1, 3, 2, 5, 4] )) # 8

# sticker = 1~100,000
