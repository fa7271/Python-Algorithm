import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10 ** 6)

T = int(sys.stdin.readline())

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    number = numbers[x]

    # 이미 방문한 노드인 경우 (사이클 가능 여부 판단)
    if visited[number] == True:
        if number in cycle:  # 사이클이 존재하는 경우
            result += cycle[cycle.index(number):]  # 사이클을 이루는 구간부터 팀을 이룸
        return
    else:
        dfs(number)  # 방문하지 않은 노드인 경우 계속해서 탐색 진행

# 테스트 케이스 수만큼 반복
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    numbers = [0] + list(map(int, input().split()))
    visited =[False]* (N+1)
    result = []  # 사이클을 이루는 노드들을 저장하는 리스트 초기화

    # 모든 노드에 대해서 사이클 탐색
    for i in range(1, N+1):
        if not visited[i]:  # 아직 방문하지 않은 노드인 경우에만 탐색 시작
            cycle = []  # 사이클을 이루는 노드들을 저장하는 리스트 초기화
            dfs(i)

    print(N - len(result))  # 사이클을 이루는 노드 수를 제외한 팀의 수 출력
