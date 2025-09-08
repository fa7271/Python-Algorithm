import sys
sys.stdin = open('/Python/h.txt', 'r')



n = int(input())


line = 1        # 1부너 N번 방까지 최소 개수
regulation = 1  # 6씩 더할 변수
if n == 1:      # 정가운데 n = 1
    print(1)    # n = 1 출력
else:
    while True:                     #True 일떄까지 출력
        if n <= regulation:         #입력받은수가 규칙보다 작거나 같을때
            print(line)             # 최소방의 갯수 출력후
            break                   # break
        else:                       # n이 규칙보다 작을떄
            regulation += (6 * line)   #6xline
            line += 1                  #line 1 추가

