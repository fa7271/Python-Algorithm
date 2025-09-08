import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())  # 학생의 수 n을 입력 받음

lst = list(map(int, sys.stdin.readline().split(" ")))  # 학생들의 점수를 리스트 lst에 저장

if n <= 1:  # 학생의 수가 1 이하라면 두 명 이하로 조를 편성할 수 없음
    print(0)
    exit(0)

dp = [0] * (n+1)  # 동적 계획법을 위한 dp 리스트 초기화

for i in range(1, n+1):  # 각 학생들을 순서대로 추가하며 최적의 조합을 찾음
    max_v, min_v = 0, 10001  # 현재까지 선택한 학생들의 가장 높은 점수와 가장 낮은 점수 초기화

    for j in range(i, 0, -1):  # 현재까지 선택한 학생들 중에서 가장 나이가 어린 학생부터 순서대로 확인
        max_v = max(max_v, lst[j-1])  # 현재까지 선택한 학생들 중 가장 높은 점수를 max_v에 저장
        min_v = min(min_v, lst[j-1])  # 현재까지 선택한 학생들 중 가장 낮은 점수를 min_v에 저장
        dp[i] = max(dp[i], max_v - min_v + dp[j - 1])  # dp[i]는 현재까지 선택한 학생들로 이루어진 조에서 가장 점수가 높은 학생과 가장 점수가 낮은 학생의 차이와, 이전 조까지의 잘 짜여진 정도를 더한 값으로 갱신
        print(i,j, max_v,min_v,dp)

print(dp[n])  # 조가 잘 짜여진 정  도의 최댓값 출력
