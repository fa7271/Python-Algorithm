import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')
# input = sys.stdin.readline


array = list()
for i in range(2, 246913):                  # 범위 설정
    count = 0

    for j in range(2, int(i**0.5)+1):       # 2n의 제곱근
        if i % j == 0:                      # 소수 아닌거 찾고
            count += 1                      # 소수면 카운트 올림
            break

    if count == 0:                          # 소수 이면
        array.append(i)                     # 리스트에 추가

while True:
    n = int(input())                       # 입력받은수
    result = 0                             # 갯수 선언

    if n == 0 :                            # 입력받은수가 0 이면 브레이크
        break

    for i in array:                        # 위에 만든 리스트(소수) 안에서 찾음
        if n<i<=2*n:                       # 범위 정해줌
            result +=1                     # 범위 안에 있으면 result +1
    print(result)




    # array = [True for _ in range(2 * n + 1)]
    #
    # for i in range(2, int(math.sqrt(2 * n)) + 1):
    #     if array[i]:
    #         j = 2
    #         while i * j <= 2 * n:
    #             array[i * j] = False
    #             j += 1
    #
    # count = 0

#각 테스트 케이스에 대해서,
# n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.