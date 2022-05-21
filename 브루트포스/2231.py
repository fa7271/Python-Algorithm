import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

n = int(input())
res = 0                             # 결과값

for i in range(1,n+1):              # 1부터 받은 숫자까지 범위 설정
    N = sum(list(map(int,str(i))))  # 각 자릿수 합
    a = i+N                         # 생성자 구하기
    if(a == n):                     # 받은 값과 생성자가 같을떄
        res = i                     # 결과값 설정
        break                       # 포문 탈출
print(res)

