import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N, K, M = map(int,sys.stdin.readline().rstrip().split(" "))

# 김밥 손질
arr = []
for _ in range(N):
    kim = int(input().rstrip())
    #꼬다리 * 2 보다 크면 자를 수 있 손질된 김밥 길이 arr에 저장
    if kim > K*2:
        arr.append(kim-(2*K))
    # 김밥 길이보다 길거나 1개 밖에 안잘릴경우
    elif kim - K > 0 and kim < 2 * K:
        arr.append(kim-K)
arr.sort()
# 자른게 없음
if len(arr) == 0:
    print(-1)
    exit()

res = -1
left,right = 1,arr[-1]

while left <= right:

    mid = ( left + right ) // 2 # 김밥 최대 길이저장
    total = sum([i//mid for i in arr]) # 각 길이마다 몫을 더해줌
    if total < M: # 몫이 원하는 M보다 작으면 최댓값이 작아져야함
        right = mid-1
    else: # 반대 맞는경우도 있으니 res도 최신화
        left = mid+1
        res = mid

print(res)

