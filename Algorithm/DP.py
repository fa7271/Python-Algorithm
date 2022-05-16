



dp = [0]*100            # 방생성

dp[1]=1
dp[2]=1
n=99
# bottom up 방식
for i in range(3, n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])

############################################################################################
#Topdown 방식
memo = [0]*100          # 방 생성

def fibo(x):            #topdown 방식
    if x==1 or x==2:
        return 1
    if memo[x] != 0:    #이미 방이 차 있으면 그대로 반환
        return memo[x]
    # 점화식 생성
    memo[x] = fibo(x-1)+fibo(x-2)  #아직 계산하지 않았다면 결과에 따라 방을 채운다
    return memo[x]
print(fibo(99))