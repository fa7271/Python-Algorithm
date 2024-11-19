import sys

# 테스트 입력 파일 경로 설정
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# 입력 받기
n, m = map(int, sys.stdin.readline().rstrip().split())
r, c, direction = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# 북, 동, 남, 서 방향 정의
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 청소 방문 처리 배열
visited = [[0] * m for _ in range(n)]
visited[r][c] = 1  # 시작 위치 청소

# 청소한 구역 수
res = 1

while True:
    clean = False

    # 현재 방향을 기준으로 반 시계 방향으로 회전하며 탐색
    for i in range(4):
        direction = (direction + 3) % 4  # 반 시계 방향 회전
        nx, ny = r + move[direction][0], c + move[direction][1]

        # 청소하지 않은 구역이 있고, 이동 가능할 때
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1  # 청소 표시
            r, c = nx, ny  # 위치 이동
            res += 1  # 청소한 칸 수 증가
            clean = True
            break
    # 네 방향 모두 청소가 되어 있는 경우
    if not clean:
        # 후진 위치 계산
        back_direction = (direction + 2) % 4
        r, c = r + move[back_direction][0], c + move[back_direction][1]

        # 후진했을 때 벽이면 종료
        if graph[r][c] == 1:
            break
# 결과 출력
print(res)
