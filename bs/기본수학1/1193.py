import sys
sys.stdin = open('/Python/h.txt', 'r')

n = int(input())
line = 1

while n > line:             # 입력받은 수가 몇번째 라인에 있는지 확인
    n -= line
    line += 1
if line%2==0:               # 라인이 짝수라면
    a = n
    b = line-n+1
else:                       # 라인이 홀수라면
    a=line-n+1
    b=n
print(a,"/",b,sep='')


