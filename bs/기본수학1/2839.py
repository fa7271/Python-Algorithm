import sys
sys.stdin = open('/Python/h.txt', 'r')

n = int(input())
count = 0
while n >=0:
    if n%5==0:                      # 5의 배수 확인
        count+=(n//5)               # 5의 배수면 몫만큼 카운트
        print(count)
        break
    n -= 3                          # 5의 배수가아니면 3씩 빼주고
    count += 1                      # count 를 계속 올려줌
else:                           # 계속 해줘도 5의 배수가 안되고 n 이 0보다 작아지면
    print(-1)                   # -1 을 출력
