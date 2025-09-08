def solution(money):
    firsthome_dp = [0] * len(money)
    secondhome_dp = [0] * len(money)

    # 첫 집 털었을경우
    firsthome_dp[0] = money[0]
    firsthome_dp[1] = money[0]
    for i in range(2,len(money)-1):
        firsthome_dp[i] = max(firsthome_dp[i-2] + money[i],firsthome_dp[i-1])

    # 첫 집 안 털었을 경우
    secondhome_dp[1] = money[1]
    for i in range(1,len(money)):
        secondhome_dp[i] = max(secondhome_dp[i-2]+money[i],secondhome_dp[i-1])

    return max(firsthome_dp[-2], secondhome_dp[-1])
print(solution([1, 2, 3, 1]))