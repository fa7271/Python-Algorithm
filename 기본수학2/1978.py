import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

N = int(input())
array = list(map(int,input().split()))
count = 0
for i in array:                    #   array에 있는 숫자 빼옴
    if i != 1:                     #   1이 아닐떄 실행
        for k in range(2,i):       #   k는 1과 자기자신을 제외한 수로 나눴을때
            if i % k ==0:          # 나눠지는게 있으면 브레이크 하고 나옴
                break
        else:                      #나눠지는게 없으면
            count +=1              # count +1
print(count)








