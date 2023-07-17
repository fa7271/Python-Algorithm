import sys
from itertools import permutations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


N = int(sys.stdin.readline())
num = list(permutations([str(i) for i in range(1,10)],3))
for _ in range(N):
    n, s, b = map(int, input().split())
    n = list(str(n))
    rmcnt = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= rmcnt # num[0] 부터 시작
        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1
        if (strike != s) or (ball != b):
            num.remove(num[i])
            rmcnt += 1

print(len(num))


import sys
from itertools import permutations

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())  # 테스트 케이스의 개수 입력
num = list(permutations([str(i) for i in range(1, 10)], 3))  # 1부터 9까지 순열 생성

for _ in range(N):
    n, s, b = map(int, input().split())  # 입력된 정수와 스트라이크, 볼 개수 입력
    n = list(str(n))  # 입력된 정수를 리스트로 변환
    rmcnt = 0  # 삭제된 요소의 개수를 저장하는 변수
    i = 0  # 인덱스 변수

    while i < len(num):  # num 리스트의 인덱스 범위 내에서 반복
        strike = ball = 0  # 스트라이크와 볼의 개수를 초기화
        curr_num = num[i]  # 현재 순열

        for j in range(3):  # 각 자리에 대해 스트라이크와 볼 개수 계산
            if curr_num[j] == n[j]:  # 자릿수와 값이 일치하는 경우 스트라이크 증가
                strike += 1
            elif n[j] in curr_num:  # 값은 일치하지 않지만 다른 자릿수에 포함된 경우 볼 증가
                ball += 1

        if (strike != s) or (ball != b):  # 입력된 스트라이크, 볼 개수와 일치하지 않는 경우
            num.pop(i)  # 현재 인덱스의 순열을 삭제하고 다음 인덱스로 이동하지 않음
            rmcnt += 1  # 삭제된 요소 개수 증가
        else:
            i += 1  # 다음 인덱스로 이동하여 검사

print(len(num))  # 남은 순열의 개수 출력
