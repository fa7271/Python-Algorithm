import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k = map(int, sys.stdin.readline().split())
numbers = list(map(int, str(n)))
m = len(numbers)

if m == 1 or (m == 2 and numbers[1] == 0):
    print(-1)
    exit()

# BFS를 사용하여 탐색
def bfs():
    queue = deque([(numbers, 0)])
    visited = set()
    visited.add((tuple(numbers), 0))
    max_result = -1

    while queue:
        current, depth = queue.popleft()

        if depth == k:  # K번 교환 완료 시
            max_result = max(max_result, int("".join(map(str, current))))
            continue

        for i in range(m):
            for j in range(i + 1, m):
                if i == 0 and current[j] == 0:
                    continue

                # 교환
                next_state = current[:]
                next_state[i], next_state[j] = next_state[j], next_state[i]

                if (tuple(next_state), depth + 1) not in visited:
                    visited.add((tuple(next_state), depth + 1))
                    queue.append((next_state, depth + 1))

    return max_result

result = bfs()
print(result)
