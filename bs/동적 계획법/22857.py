import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# n,m = map(int,sys.stdin.readline().split(" "))
# S = list(map(int,sys.stdin.readline().split(" ")))
#
# #투 포인터 방법
# start, end, count, res = 0, 0,0,0
# result = -1e9
# flag = 1
# for i in range(n):
#     while count <= m and end <= n-1:
#         # 홀수 일때
#         if S[end] % 2:
#             # 홀수 의 숫자가 m개 이면
#             if count == m:
#                 # 다 지운거니깐 브레이크
#                 break
#             # 아직 m개가 아니면 홀수 갯수 증가
#             count += 1
#         # 홀수든 짝수든 길이 증가
#         res += 1
#         # end 끝 도달 도착시
#         end += 1
#
#     # 가장 긴 길이 최댓값 넣어주고
#     result = max(result,res-count)
#     # 이제 start 를 증가시켜주면서 비교해야함
#     # 홀수
#     if S[i] % 2:
#         # 홀수 갯수 늘린거 하나 빼주고
#         count -= 1
#     # 홀수든 짝수든 길이 증가해준거 하나 빼줌
#     res -= 1
# print(result)

n, k =list(map(int,input().split()))
s = [0] + list(map(int,input().split()))
dp = [[0]*(k+1) for _ in range(n+1)] # [처음부터i까지][삭제횟수]
for i in range(1,n+1):
    for k in range(k+1):
        # 짝수인 경우
        if s[i] % 2 == 0:
            # 삭제횟수는 안 늘어남, 수열길이는 늘어남
            # 이전 수열 까지의 길이 + 1
            dp[i][k] = dp[i-1][k] + 1
        # 홀수인경우 k = 0 일 경우삭제 작업을 아직 한 번도 수행하지 않았다는 뜻 홀수인수를 삭제해도 현재까지의 연속 부분 수열에는 영향을 주지 않는다,
        if k != 0 and s[i] % 2:
            # 이전 상태에서 k-1번의 삭제 횟수를 사용한 경우의 값 >> s[i]를 삭제를 했다는 뜻
            dp[i][k] = dp[i-1][k-1]
res = []
for i in dp:
    res.append(i[k])
print(max(res))
