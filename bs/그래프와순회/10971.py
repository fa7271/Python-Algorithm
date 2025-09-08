import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())
costs = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N  # 방문
cost = 0
ans = sys.maxsize

def dfs(x, y):
    global cost, ans

    if x == N-1:  # 모든 도시를 방문한 경우
        if costs[y][0]:  # 마지막 도시에서 출발 도시로 돌아가는 값이 0이 아니면
            cost += costs[y][0]  # 더해주고
            ans = min(ans, cost)  # 최솟값 최신화
            cost -= costs[y][0]  # 다른 경로도 확인해야 하므로 빼준 뒤 리턴
        return

    for i in range(1, N):  # 1부터 N-1까지의 도시를 선택
        if visited[i] == 0 and costs[y][i]:  # 방문하지 않은 도시이고, 이동 가능한 경우
            visited[i] = 1  # 해당 도시를 방문 표시
            cost += costs[y][i]  # 비용 추가
            dfs(x+1, i)  # 다음 도시로 이동
            visited[i] = 0  # 이전에 방문한 도시를 방문 가능한 도시로 변경
            cost -= costs[y][i]  # 비용 제거


dfs(0, 0)  # 시작 도시인 0번 도시에서 순회 시작
print(ans)  # 최소 비용 출력
