import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

(N,M) = map(int,(input().split()))

# print(N,M)
chess = []                          # 체스판
new = []                            # count 해야할 갯수
for i in range (N):                 # 8x8짜리 chess 체스판 만들기
    x = input()
    chess.append(x)
                                    # M,N 이 8 이상일 경우
for i in range(N-7):                # 8*8 자르기위해 -7해줌
    for j in range(M-7):            #
        W = 0                       # w 로 색칠 해줘야하는 것 초기화
        B = 0                       # B 로 색칠 해줘야하는 것 초기화
        for k in range(i,i+8):                # 시작지점
            for l in range(j,j+8):            # 시작지점
                if (k + l) % 2 == 0:        #  짝수인경우
                    if chess[k][l] != 'W':  #  시작 점이 블랙일때
                        W = W + 1           #  화이트 갯수 증가
                    if chess[k][l] != 'B':
                        B = B + 1
                else:                        # 홀수 일때
                    if chess[k][l] != 'B':   #
                        W = W + 1
                    if chess[k][l] != 'W':
                        B = B + 1
        new.append(W)
        new.append(B)
print(min(new))

# ((k+l)/2) 가 홀수 인 경우도 일정한 색을 가지고 짝수 인 경우도 일정한 색을 가진다

