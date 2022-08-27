import sys
sys.stdin = open('/Python/h.txt', 'r')


N = int(input())
fix = 666                                   #처음 666인 수
while True:                               # N 이 0이 아니면 계속 반복
    if '666' in str(fix):                   # 만약 666이란 문자열이 있으면
        N = N-1                             # 카운트 감소
        if N == 0:                          # 만약 N 이 0이면
            break                           # 포문 탈출 후 출력.
    fix = fix + 1                           #first의 값을 1 증가시킨다.
print(fix)