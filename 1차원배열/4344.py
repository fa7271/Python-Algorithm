import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

n = int(input())
for i in range(n):
    a = list(map(int,input().split(" ")))
    avg = sum(a[1:])/a[0]            # list 로 했기 때문에 인덱싱 가능  a[1]부터 a[n까지] a[o]으로 나눔
    count = 0                        # count  0 으로 선언
    for j in range(1,len(a)):        # 1부터 a에 길이만큼 for 문 돌림
        if a[j] > avg:               # a[i]가 평균보다 높으면
            count += 1               # 카운트 += 1
    result = count / a[0] * 100      # 평균을 넘는 비율 구하는 평균보다 높은 사람수 / 총 인원 * 100
    print('%.3f'% result + '%')      # %.3f 소수점 3자리 까지 출력해라


