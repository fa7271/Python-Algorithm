import sys
sys.stdin = open('/Python/h.txt', 'r')


N = int(input())
i = 2               # 제일 작은 나누는 수 선언
while N != 1:       # 입력받은 수 1이 아닐떄
    if N%i ==0:     # N 나누기 i 의 몫이 0 >> 즉 2의배수일때
        N /= i      # N은 2로 나누고 다시 N에 저장
        print(i)    # 2출력
    else:           # 2의 배수가 아니면
        i +=1       # 최소공배수를 +1
    if i>N:         # 쭉 진행하다가 최소공배수보다 바뀌는 N보다 클떄
        break       # for문 탈출
