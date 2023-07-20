import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


#곡의 개수, 시작볼륨, M
# N, S, M = map(int,sys.stdin.readline().rstrip().split(" "))
# arr =list(map(int,sys.stdin.readline().split(" ")))
# dp = [0] * (len(arr)+1)
# P = dp[0] = arr[0]
#
# for i in range(1,len(arr)+1):
#     if 0 < max(dp[i-1]+arr[i-1], dp[i-1]-arr[i-1]) <= M:
#         dp[i] = max(dp[i-1]+arr[i-1], dp[i-1]-arr[i-1])
# print(max(dp))
# 0보다 작은 값으로 볼륨을 바꾸거나, M보다 큰 값


N, S, M = map(int,sys.stdin.readline().rstrip().split(" "))

arr = list(map(int, input().split()))
dp = [[0] * (M+1) for _ in range(N+1)]

# 시작볼륨 설정
dp[0][S] = 1

for i in range(1,N+1): #곡의 개수 만큼
    for j in range(M+1):
        # 볼륨이 1이면
        if dp[i-1][j] == 1:
            # 그 다음 볼륨을 체크한다.
            if 0 <= j+arr[i-1] <= M:
                dp[i][j+arr[i-1]]=1
            if 0 <= j-arr[i-1] <= M:
                dp[i][j-arr[i-1]] = 1

for i in range(M, -1, -1):
    if dp[N][i]==1:
        ans = i
        break
print(ans)



