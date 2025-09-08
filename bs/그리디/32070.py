import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, rank, cnt, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            root_a, root_b = root_b, root_a

        parent[root_a] = root_b
        cnt[root_b] += cnt[root_a]

        if rank[root_a] == rank[root_b]:
            rank[root_b] += 1

def solve():

    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    ball_location = [[] for _ in range(n + 1)]

    index = 1

    for i in range(1, n + 1):
        a, b = map(int, data[index:index + 2])
        ball_location[a].append(i * 2)
        ball_location[b].append(i * 2 + 1)
        index += 2

    print(ball_location)
    parent = [i for i in range(n+1)]

    rank = [1] * (n + 1)
    cnt = [1] * (n + 1)
    top_of_box_pair = [0] * (n + 1)
    solved = [False] * (n + 1)


    for i in range(1, n + 1):
        union(parent, rank, cnt, ball_location[i][0] // 2, ball_location[i][1] // 2)

    for i in range(1, n + 1):
        # 둘다 박스 위에 있을경우
        if ball_location[i][0] % 2 == 0 and ball_location[i][1] % 2 == 0:
            # 같은 사이클인지 확인함
            root_idx = find(parent, ball_location[i][0] // 2)
            top_of_box_pair[root_idx] += 1

    for i in range(1, n + 1):
        # 박스 위에 있는 애들 사이클 확인
        root_idx = find(parent, ball_location[i][0] // 2)
        # 2개 이상이면 와리가리로 못 만듦
        if top_of_box_pair[root_idx] >= 2:
            print(-1)
            return

    ans = 0
    for i in range(1, n + 1):
        root_idx = find(parent, ball_location[i][0] // 2)
        if solved[root_idx]:
            continue
        solved[root_idx] = True
        x = cnt[root_idx]
        if x >= 2:
            ans += x + 1
    #         x = 1 이면 같은 색끼리 가지고 있음
    print(ans)
solve()