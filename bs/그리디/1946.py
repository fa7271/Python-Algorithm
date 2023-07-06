import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    applicants = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    applicants.sort(key=lambda x: x[0])  # 서류심사 순위를 기준으로 오름차순 정렬

    cnt = 1
    min_interview_rank = applicants[0][1]  # 첫 번째 지원자의 면접 순위를 저장
    for i in range(1, N):
        if applicants[i][1] < min_interview_rank:
            min_interview_rank = applicants[i][1]  # 면접 순위를 갱신
            cnt += 1
    print(cnt)


