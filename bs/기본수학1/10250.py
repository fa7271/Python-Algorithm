import sys
sys.stdin = open('/Python/h.txt', 'r')

T = int(input())
# H 층수 W = 방수 N = 손님
for i in range(T):
    H,W,N = list(map(int,input().split()))
    num = (N//H +1)                          #라인 = (N//H)+1 라인
    line = N%H                               # % 나머지반환
    if line == 0:                             #층이 H의 배수이면
        num = N//H
        line = H
    print(line*100+num)

