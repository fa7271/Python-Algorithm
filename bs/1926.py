import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# 입력 파일에서 n과 m 값을 읽어옵니다.
n, m = map(int, sys.stdin.readline().split())

# 그래프를 표현하기 위해 2차원 리스트인 graph를 생성합니다.
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# 이동 방향을 나타내는 리스트입니다.
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

# 방문 여부를 나타내기 위한 2차원 리스트입니다.
visited = [[False] * m for _ in range(n)]

# 연결된 구성 요소의 개수를 세기 위한 변수입니다.
pic = 0

# BFS 함수를 정의합니다.
def bfs(x, y):
    q = deque([(x, y)])  # 시작 위치를 큐에 추가합니다.
    visited[x][y] = True  # 시작 위치를 방문했다고 표시합니다.
    cnt = 1  # 방문한 노드의 개수를 세기 위한 변수입니다.

    # 큐가 빌 때까지 반복합니다.
    while q:
        a, b = q.popleft()  # 큐에서 위치를 꺼냅니다.

        # 이동할 수 있는 모든 방향에 대해 확인합니다.
        for dx, dy in move:
            nx = dx + a
            ny = dy + b

            # 다음 위치가 그래프 내에 있고, 연결된 구성 요소에 속하며 아직 방문하지 않았다면,
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True  # 다음 위치를 방문했다고 표시합니다.
                q.append((nx, ny))  # 다음 위치를 큐에 추가합니다.
                cnt += 1  # 방문한 노드의 개수를 1 증가시킵니다.

    return cnt  # BFS를 마친 후 방문한 노드의 개수를 반환합니다.

cnt = 0  # 연결된 구성 요소의 개수를 세기 위한 변수입니다.
lst = 0  # 가장 큰 구성 요소의 크기를 저장하기 위한 변수입니다.

# 모든 위치를 순회하면서 연결된 구성 요소를 탐색합니다.
for i in range(n):
    for j in range(m):
        # 현재 위치가 연결된 구성 요소에 속하고 아직 방문하지 않았다면,
        if graph[i][j] == 1 and not visited[i][j]:
            lst = max(lst, bfs(i, j))  # BFS를 수행하고 가장 큰 구성 요소의 크기를 업데이트합니다.
            cnt += 1  # 연결된 구성 요소의 개수를 1 증가시킵니다.

print(cnt)  # 연결된 구성 요소
print(lst)  # 최대 그림갯수