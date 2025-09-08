import sys
from itertools import permutations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

K,M = map(int,input().split(" "))
MAX = 10**6    # K개의 숫자를 고를 때 나올 수 있는 가장 큰 수

prime_lst = [True] * (10**K)
MAX = int((10**K)**0.5)
for i in range(2, MAX + 1):
    if prime_lst[i]:
        for j in range(i+i, 10**K, i):
            prime_lst[j] = False
count=0
for ii in permutations(range(10),K):
    # 시작 0이면 제낌
    if ii[0] == 0 :
        continue
    N = int(''.join(list(map(str, ii))))   # 숫자 조합
    temp = N
    # 조건 2 M 으로 나눠줌
    while temp % M == 0:
        temp //= M
    idx = 2 # 케이스2번 하기 위함
    # 소수의 곱을 위해서 범위 설정
    while idx <= int(temp**0.5):
        # 나누어 떨어지면 체크
        if temp % idx == 0 :
            # 두 소수의 합으로 이루어 졌으면
            if prime_lst[idx] and prime_lst[temp//idx]:
                #1번 조건 확인해봄
                check_one = 2
                # 1번조건에서 절반까지 확인하면 전체 다 확인하는것임
                while check_one < N//2 :
                    # 두개다 소수면
                    if prime_lst[check_one] and prime_lst[N-check_one]:
                        # 2개 조건 만족한거임
                        count += 1
                        # 더이상 2번 꺼 안 해도되니까 break
                        break
                    check_one += 1
            break # 이미 조건 성립했으니깐 다음꺼 하러 감
        idx +=1
print(count)

#1. 서로 다른 두 개의 소수의 합으로 나타낼 수 있는 경우
#2. M으로 나누어 떨어지지 않을때까지 나눈 수가 두 개의 소수의 곱인 경우, 이 때, 두 개의 소수가 같아도 된다.


