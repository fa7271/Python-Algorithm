import sys
sys.setrecursionlimit(10**7)

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

graph = [list(map(int, list(input().strip()))) for _ in range(8)]
visited = [[False] * 7 for _ in range(8)]
domino_used = [[False] * 7 for _ in range(7)]
directions = [(0, 1), (1, 0)]

def backtrack(x, y):
    if x == 8:  # 모든 줄 탐색 완료
        return 1

    nx, ny = (x, y + 1) if y < 6 else (x + 1, 0)
    if visited[x][y]:  # 이미 방문한 칸이면 넘어가기
        return backtrack(nx, ny)

    result = 0
    visited[x][y] = True
    current = graph[x][y]

    # 도미노 배치 시도
    for dx, dy in directions:
        adj_x, adj_y = x + dx, y + dy
        if 0 <= adj_x < 8 and 0 <= adj_y < 7 and not visited[adj_x][adj_y]:
            adj_value = graph[adj_x][adj_y]
            if not domino_used[current][adj_value]:
                domino_used[current][adj_value] = domino_used[adj_value][current] = True
                visited[adj_x][adj_y] = True

                result += backtrack(nx, ny)

                # 복구
                domino_used[current][adj_value] = domino_used[adj_value][current] = False
                visited[adj_x][adj_y] = False

    visited[x][y] = False
    return result

print(backtrack(0, 0))
