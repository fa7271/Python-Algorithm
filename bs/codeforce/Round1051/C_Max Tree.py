import sys

sys.stdin = open('/Users/song/Desktop/Python/h.txt', 'r')

import sys
import collections

def solve():
    """하나의 테스트 케이스를 해결하는 함수"""

    # 1. 정점의 개수 n을 입력받습니다.
    try:
        n_str = sys.stdin.readline()
        if not n_str: return
        n = int(n_str)
    except (IOError, ValueError):
        return

    # 2. 그래프와 진입 차수(in-degree)를 저장할 자료구조를 초기화합니다.
    # graph: 각 정점에서 나가는 이웃 정점들을 저장 (방향 그래프)
    # in_degree: 각 정점으로 들어오는 화살표의 개수
    graph = collections.defaultdict(list)
    in_degree = [0] * (n + 1)  # 1번부터 n번 정점까지 사용하기 위해 n+1 크기로 생성

    # 3. n-1개의 간선 정보를 입력받아 방향 그래프를 구성합니다.
    for _ in range(n - 1):
        u, v, x, y = map(int, sys.stdin.readline().split())

        # 가중치를 비교하여 더 큰 값을 얻는 방향으로 화살표(간선)를 설정합니다.
        if x > y:
            # p_v < p_u 관계를 원하므로 v -> u 방향의 간선을 추가합니다.
            graph[v].append(u)
            in_degree[u] += 1
        else:
            # p_u < p_v 관계를 원하므로 u -> v 방향의 간선을 추가합니다.
            graph[u].append(v)
            in_degree[v] += 1

    print(in_degree, graph)

    # 4. 위상 정렬을 위한 큐를 초기화합니다.
    # 진입 차수가 0인 모든 정점(순서의 시작점이 될 수 있는 후보)을 큐에 넣습니다.
    queue = collections.deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
    # 5. 위상 정렬을 수행합니다.
    topological_order = []
    while queue:
        # 큐에서 정점을 하나 꺼내 순서 리스트에 추가합니다.
        node = queue.popleft()
        topological_order.append(node)

        # 현재 정점에서 나가는 모든 간선을 확인합니다.
        for neighbor in graph[node]:
            # 연결된 이웃 정점의 진입 차수를 1 줄입니다.
            in_degree[neighbor] -= 1
            # 진입 차수가 0이 되었다면, 새로운 시작점이 될 수 있으므로 큐에 추가합니다.
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 6. 위상 정렬된 순서에 따라 값을 할당하여 최종 순열 p를 만듭니다.
    p = [0] * (n + 1)
    print(topological_order)
    for i, node_num in enumerate(topological_order):
        # 정렬된 순서대로 1, 2, 3, ... 값을 부여합니다.
        value_to_assign = i + 1
        p[node_num] = value_to_assign

    # 7. 결과를 문제 형식에 맞게 출력합니다.
    print(*p[1:])


def main():
    """전체 테스트 케이스를 처리하는 메인 함수"""
    try:
        # 첫 줄에서 테스트 케이스의 수를 읽습니다.
        num_test_cases = int(sys.stdin.readline())
    except (IOError, ValueError):
        num_test_cases = 0

    for _ in range(num_test_cases):
        solve()

if __name__ == "__main__":
    main()