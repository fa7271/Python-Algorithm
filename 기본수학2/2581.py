import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

M = int(input())
N = int(input())

sum = 0
list = list()                   # M 과 N 차이에서 나오는 소수들 젛기위한 리스트 생성
for i in range(M,N+1):
    if i != 1:
        for k in range(2,i):    #소수가 아니라면
            if i % k ==0:
                break           #브레이크로 포문 탈출
        else:                   #소수라면
            sum += i            #sum 에 더해서 다시 sum으로 만들어주고
            list.append(i)      #list에 그 숫자를 추가 해준다.
if len(list) == 0:              #만약 list에 길이가 0 즉 소수가 없을떄
    print('-1')                 # -1 을 출력해주고
else:
    print(sum,min(list))        # 소수가 있으면 소수들의 합과 소수의 갯수 출력








