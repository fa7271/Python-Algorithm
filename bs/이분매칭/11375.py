import sys

sys.setrecursionlimit(100000)
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m = map(int, input().split())
task = [list(map(int, input().split()))[1:] for _ in range(n)]
visit = [-1] * (m + 1)


# x번째 사람을 작업에 배정
def dfs(x):
    # x번째 사람이 할 수 있는 작업 i에 대해 반복
    for i in task[x]:
        # i번째 작업이 아직 확인되지 않았다면
        if not check[i]:
            # i번째 작업을 이번 탐색에서 이미 확인했음을 표시 (중복 탐색 방지)
            check[i] = True
            # i번째 작업이 아직 배정되지 않았거나, 이미 배정된 사람이 다른 작업을 맡을 수 있는 경우
            if visit[i] == -1 or dfs(visit[i]):
                # i번째 작업을 x번째 사람에게 배정
                visit[i] = x
                return True
    # x번째 사람이 작업을 맡을 수 있으면 True, 그렇지 않으면 False 반환
    return False


result = 0

for i in range(n):
    check = [False] * (m + 1)
    if dfs(i):
        result += 1
    print(visit)
print(result)
