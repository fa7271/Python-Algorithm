import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

C = int(input())  # 테스트 케이스의 수를 입력받습니다.

def bt(player, point):
    global max_point

    if player == 11:  # 모든 선수를 배치한 경우
        max_point = max(max_point, point)  # 현재까지의 점수를 최대 점수와 비교하여 갱신
        return

    for i in range(11):  # 각 선수별로 포지션을 선택하는 반복문
        if visited[i] or not player_points[player][i]:  # 이미 방문한 포지션이거나 해당 포지션의 점수가 0인 경우
            continue  # 가지치기: 다음 포지션으로 넘어감

        visited[i] = 1  # 현재 포지션에 선수를 배치했음을 표시
        bt(player + 1, point + player_points[player][i])  # 다음 선수를 선택하러 재귀 호출
        visited[i] = 0  # 백트래킹: 포지션을 원래대로 되돌림

for i in range(C):
    max_point = 0
    player_points = [list(map(int, input().split())) for _ in range(11)]  # 각 선수의 포지션 별 점수 입력
    visited = [0 for _ in range(11)]  # 각 포지션의 방문 여부를 기록할 배열 초기화
    bt(0, 0)  # 백트래킹 함수 호출을 통해 최대 점수 계산
    print(max_point)  # 최대 점수 출력


