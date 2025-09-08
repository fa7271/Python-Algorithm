import collections
import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())  # 지동이 방에 출입한 모기의 마릿수 N을 입력 받음
lst = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(N)]  # 모기의 입장 시각과 퇴장 시각을 입력 받아 2차원 리스트로 저장

dic = collections.defaultdict(int)  # 각 시간대에 대한 누적 모기 수를 저장하기 위한 딕셔너리 생성
for left, right in lst:
    dic[left] += 1  # 입장 시각에 대한 모기 수를 1 증가
    dic[right] -= 1  # 퇴장 시각에 대한 모기 수를 1 감소

times = sorted(dic.keys())  # 딕셔너리의 키를 정렬하여 시간대를 얻음
cnt = 0  # 모기가 가장 많이 있는 시간대의 모기 마릿수를 저장할 변수
res = [0, 0]  # 모기가 가장 많이 있는 시간대의 시작 시각과 끝 시각을 저장할 리스트

mogi = 0  # 현재 시간대에서의 누적 모기 수를 저장할 변수
check = False  # 모기가 가장 많이 있는 시간대의 시작 시각인지 확인하기 위한 변수

for time in times:
    mogi += dic[time]  # 현재 시간대에서 모기 수를 누적
    if mogi > cnt:  # 누적 모기 수가 최대값보다 큰 경우
        cnt = mogi  # 최대값을 갱신
        res[0] = time  # 시작 시각을 갱신
        check = True  # 시작 시각이 갱신됨을 표시
    elif mogi < cnt and check:  # 누적 모기 수가 최대값보다 작고, 시작 시각이 갱신된 경우
        res[1] = time  # 끝 시각을 갱신
        check = False  # 끝 시각이 갱신됨을 표시

print(cnt)  # 모기가 가장 많이 있는 시간대의 모기 마릿수 출력
print(*res)  # 모기가 가장 많이 있는 시간대의 시작 시각과 끝 시각을 출력