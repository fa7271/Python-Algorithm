import sys
sys.stdin = open('/Python/h.txt', 'r')


# “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의
# 합만큼 사람들을 데려와 살아야 한다”

n = int(input())                          # 테스트케이스 갯수
for i in range(n):
    k = int(input())                      #층수
    n = int(input())                      #호수
    result = [i for i in range(1,n+1)]    # for문 값을 변수 i 에다가 담음
    for j in range(k):                    # 만약에 k = 2 이면
        for x in range(1,n):              # range(1,3)
            result[x] += result[x-1]      # j = 1일때 result[1] = 1   [2] = 3 [3] = 6
    print(result[n-1])                    # j = 2일때 result[1] = 1   [2] = 4 [3] = 10
                                          # j = 3일때 result[1] = 1   [2] = 5 [3] = 15


# 1층 = ((i(i+1))/2)
# 1층1호 = 1 ,102호= 1+2, 103호 = 1+2+3   > 1~n까지 합
# 2층1호 = 1 ,202호 =1+(3) , 203호 =1+3+6   >k의 배수만큼 증가후 덧셈
# 3층1호 = 1 ,302호 =1+4     303호 = 1 4 10


# a = int(input())
# for i in range(a):
#     d = []
#     k = int(input())
#     n = int(input())
#     d = [j for j in range(1, n+1)]  #포문 결과를 j에다가 담음
#     for l in range(k):              #변수 l  1부터 k 까지
#         for j2 in range(1, n):      #변수 j2 1부터 n 까지
#             d[j2] += d[j2-1]
#     print(d[n-1])