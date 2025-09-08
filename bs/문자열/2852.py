import heapq
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
team_win = 0
res_A = 0
res_B = 0

for i in range(N):
    team, time = input().split(" ")
    M, S = map(int, time.split(":"))

    if team == '1':  # 팀 A가 득점한 경우
        if team_win == 0:  # 들어오면서 이제 팀 A가 이기고 있음을 나타냄
            res_A += 48 * 60 - (60 * M + S)  # 현재 득점 시간 이후에도 팀 A가 이기고 있기 때문에 누적 시간에 추가
        team_win += 1  # 팀 A가 이기고 있음을 나타냄
        if team_win == 0:  # 이제 무승부로 될 것이므로 팀 B가 이기고 있던 시간을 처리
            if res_B > 0:  # 팀 B가 이기고 있던 시간이 있으면
                res_B = res_B - (48 * 60 - (60 * M + S))  # 득점 시간 이후에도 팀 B가 이기고 있었기 때문에 누적 시간에서 제거

    else:  # 팀 B가 득점한 경우
        if team_win == 0:
            res_B += 48 * 60 - (60 * M + S)
        team_win -= 1
        if team_win == 0:  # 이제 무승부로 될 것이므로 팀 A가 이기고 있던 시간을 처리.
            if res_A > 0:  # 팀 A가 이기고 있던 시간이 있으면
                res_A = res_A - (48 * 60 - (60 * M + S))  # 득점 시간 이후에도 팀 A가 이기고 있었기 때문에 누적 시간에서 제거합

print(str(res_A // 60).zfill(2) + ":" + str(res_A % 60).zfill(2))
print(str(res_B // 60).zfill(2) + ":" + str(res_B % 60).zfill(2))
