import sys
sys.stdin = open('/Python/h.txt', 'r')

N,M = map(int,(input().split()))        # 카드의 개수 M 넘지 말아야할 수
jack = list(map(int,input().split()))   # 카드 숫자 리스트로 만들어둠

res = 0                                     # 결과값
for i in range(N):                          # 1번째 카드
    for j in range(i+1,N):                  # 2번쨰 카드
        for k in range(j+1,N):              # 3번째 카드
            if jack[i]+jack[j]+jack[k] > M: # 1,2,3 카드 합이 500넘으면
                continue                    # 그냥 지나가고
            else:
                res = max(res,jack[i]+jack[j]+jack[k]) # res에 원래 들어 있던것과 포문 돌려서 나온것중 높은것 다시 res에 저장
print(res)









