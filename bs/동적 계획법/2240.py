import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t, w = map(int, sys.stdin.readline().split(" "))
tree = [0]
for i in range(t):
    tree.append(int(input()))
# 매번 움직였을때 안 움 직였을떄
# 1번에서 시작했을때 2번에서 시작했을때 시작은 1번
# 움직임은 30 번

# 자두나무위치, 떨어지는시간, 사용횟수
# 떨어지는 시간, 사용횟수
dp = [[0] * (w + 1) for _ in range(t + 1)]
dp[1][0], dp[1][1] = tree[1] % 2, tree[1] // 2
# 나무의 위치
for i in range(2, t+1):
    # 이동 횟수
    # 1번이 시작이므로 짝수번 움직 였으면 1번, 홀수면 2번임
    for j in range(w+1):
        x = tree[i] % 2 if j % 2 == 0 else tree[i] // 2
#         dp [i][j] = i-1번 까지 j번을 사용해서 온 최댓값 + 지금 자두 없는거
        dp[i][j] = max(dp[i-1][0:j+1]) + x
print(max(dp[-1]))

