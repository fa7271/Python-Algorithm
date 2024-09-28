import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


INF = float('inf')


# 거리 계산 함수
def dist(a, b):
    return abs(checkpoints[a][0] - checkpoints[b][0]) + abs(checkpoints[a][1] - checkpoints[b][1])


n, k = map(int, input().split())
checkpoints = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[INF] * (k + 1) for _ in range(n)]

# 아직 1개도 안 건너뜀 2개 남음
dp[0][-1] = 0

# DP 계산
# 현재 위치
for i in range(n-1) :
    # 남은 체크 포인트
    for j in range(k+1) :
        if dp[i][j] == INF :
            continue
        #    사용하는 체크 포인트 (건너 뛰기)
        for k in range(j+1) :
            # n을 넘어서 건너뜀
            if i+k+1 >= n :
                break
            dp[i+k+1][j-k] = min(dp[i+k+1][j-k], dp[i][j] + dist(i, i+k+1))
# n번째 체크포인트에서 k개의 체크포인트를 건너뛸 때 최소 거리 출력
print(min(dp[n - 1]))
