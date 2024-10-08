import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# 큰 값으로 설정 (최댓값을 구하기 위함)
INF = sys.maxsize

# 입력 받기
n = int(input())  # 도시 크기
w = int(input())  # 사건의 수
case = [(1, 1), (n, n)] + [tuple(map(int, input().split())) for _ in range(w)]
dp = [[-1] * 1002 for _ in range(1002)]  # dp[i][j]: 사건 i를 경찰차 1이, 사건 j를 경찰차 2가 처리했을 때의 최소 이동 거리
route = [[-1] * 1002 for _ in range(1002)]  # 누가 처리했는지 기록


# 두 점 사이의 거리를 계산하는 함수
def calculate(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# DP 함수
def solve(police1, police2):
    if police1 == w + 1 or police2 == w + 1:  # 모든 사건을 처리했으면 종료
        return 0

    if dp[police1][police2] != -1:  # 이미 계산된 값이면 반환
        return dp[police1][police2]

    next = max(police1, police2) + 1  # 다음 처리할 사건의 번호

    # 경찰차 1이 처리하는 경우
    dist1 = calculate(case[police1][0], case[police1][1], case[next][0], case[next][1])
    # 경찰차 2가 처리하는 경우
    dist2 = calculate(case[police2][0], case[police2][1], case[next][0], case[next][1])

    # 경찰차 1이 사건 처리
    option1 = dist1 + solve(next, police2)
    # 경찰차 2가 사건 처리
    option2 = dist2 + solve(police1, next)
    if option1 < option2:
        dp[police1][police2] = option1
        route[police1][police2] = 1  # 경찰차 1이 처리
    else:
        dp[police1][police2] = option2
        route[police1][police2] = 2  # 경찰차 2가 처리

    return dp[police1][police2]


# 사건 처리 순서 추적
def traceback(police1, police2):
    if police1 == w + 1 or police2 == w + 1:
        return

    next = max(police1, police2) + 1
    if route[police1][police2] == 1:
        print(1)
        traceback(next, police2)
    else:
        print(2)
        traceback(police1, next)


# 결과 출력
print(solve(0, 1))
traceback(0, 1)
