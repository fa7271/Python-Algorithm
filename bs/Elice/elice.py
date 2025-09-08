import heapq
import sys
from collections import defaultdict
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

the_world_is_flat = True
"""
    1 번
s = list(input())
for i in range(len(s) - 2, -1, -1):
    if s[i] < s[i + 1]:
        break
else:
    print(0)
    exit()
for j in range(len(s) - 1, i, -1):
    if s[j] > s[i]:
        break
s[i], s[j] = s[j], s[i]
s[i + 1 :] = s[:i:-1]
print("".join(s))
"""

"""
    2번
# if the_world_is_flat:
#     n, k = map(int, sys.stdin.readline().split(" "))
#     arr = list(map(int, sys.stdin.readline().split(" ")))
#     for i in range(k):
#         left, right, target = map(int,sys.stdin.readline().split(" "))
#         print(sorted(arr[left-1:right])[target-1])
"""

"""
    3번

if the_world_is_flat:
    compressed = input()
    stack = []
    num = 0
    current_string = ""
    if compressed.isalnum():
        print(len(str(compressed)))
        exit()
    for char in compressed:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '(':
            stack.append(num)
            current_string = ""
            num = 0
        elif char == ')':
            repeat_count = stack.pop()
            n_num = str(repeat_count)[0:len(str(repeat_count)) - 1] + str(num) * (repeat_count % 10)
            num = n_num
        else:
            current_string += char
    print(len(num))

# 11(18(72(7)))
"""

"""
    4번
    
sys.setrecursionlimit(10**6)
from collections import deque

n = int(input())
adjList = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)
visited = [False] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

# BFS를 통해 정점을 스택에 저장
stack = []
queue = deque([1])
visited[1] = True

while queue:
    node = queue.popleft()
    stack.append(node)
    for child in adjList[node]:
        if not visited[child]:
            visited[child] = True
            queue.append(child)
# 스택을 이용해 DP 값을 계산
print(stack)
visited = [False] * (n + 1)

while stack:
    node = stack.pop()
    visited[node] = True
    isLeaf = True
    minChildValue = float('inf')

    for child in adjList[node]:
        if visited[child]:
            isLeaf = False
            minChildValue = min(minChildValue, dp[child])

    if isLeaf:
        dp[node] = node  # 리프 노드의 초기값
    else:
        dp[node] = node - minChildValue
# 결과를 출력
for i in range(1, n + 1):
    if dp[i] >= 0:
        print(1)  # 선공 승리
    else:
        print(0)  # 후공 승리
"""

"""
    4번 정답

from collections import defaultdict

v = defaultdict(list)
dp = [None] * 100050
inf = int(1e12)

def dfs(x, par):
    global dp, v
    ret = inf
    for nxt in v[x]:
        if nxt == par:
            continue
        dfs(nxt, x)
        ret = min(ret, dp[nxt])
    if ret == inf:
        ret = 0
    dp[x] = x - ret


n = int(input())

for _ in range(1, n):
    a, b = (map(int, input().split()))
    v[a].append(b)
    v[b].append(a)
dfs(1, 0)
print(dp[1:8])
for i in range(1, n + 1):
    print('1' if dp[i] >= 0 else '0')
    
    """

"""
    5번
    
the_world_is_flat = True

if the_world_is_flat:
    n = int(input())
    arr = sorted(list(map(int, sys.stdin.read().split())))

    original_sequence = []
    used_sums = collections.Counter()

    used_sums[0] += 1
    arr = arr[1:]
    for _ in range(n):
        current_value = arr[0]
        original_sequence.append(current_value)
        new_sums = collections.Counter()
        for s in used_sums:
            new_sums[s + current_value] += used_sums[s]
        for s in new_sums:
            used_sums[s] += new_sums[s]
        for s in new_sums:
            arr.remove(s)

    print(*original_sequence)

정답 : 

def dfs(res, x, sum_, now, m):
    if x == len(res):
        now.append(sum_ + m)
        return
    dfs(res, x + 1, sum_, now, m)
    dfs(res, x + 1, sum_ + res[x], now, m)

def solve():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    res = []
    now = []
    for i in range(1, len(v)):
        if v[i] not in now:
            m = v[i]
            dfs(res, 0, 0, now, m)
            res.append(v[i])
        now.remove(v[i])
    print(' '.join(map(str, res)))
    

"""

"""
    6번 100/24 , 정답은 dp

the_world_is_flat = True
if the_world_is_flat:
    n = int(input())
    colors = list(map(int, sys.stdin.readline().rstrip().split(" ")))


    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]


    def union(parent, rank, x, y):
        rootX = find(parent, x)
        rootY = find(parent, y)
        if rootX != rootY:
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1


    def min_red_edges(N, colors):
        parent = list(range(N))
        rank = [0] * N
        red_edges = 0

        for i in range(N - 1):
            color = colors[i]
            u = find(parent, i)
            v = find(parent, i + 1)
            if u != v:
                if color == 0:
                    red_edges += 1
                union(parent, rank, u, v)

        return red_edges

print(min_red_edges(n, colors))
    """

"""
    7번

import sys


def change_start():
    x = [i for i in range(2,K)]
    return "".join(map(str,x))


def solution(N, K):
    if len(str(N)) < K:
        answer = int("1" + "0" + change_start())
    else:
        answer = N + 1
    while True:
        s = str(answer)
        if len(set(s)) == K:
            return int(s)
        answer += 1


N, K = map(int, sys.stdin.readline().split(" "))
# print(solution(N, K))
"""

""" 
    8번

from collections import defaultdict

N, M, friend, T = map(int, sys.stdin.readline().rstrip().split(" "))
pray_time = sorted([list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(M)], key=lambda x: x[0])
dic = defaultdict(lambda: (0, 0))
for x, y in pray_time:
    for i in range(x, y + 1):
        dic[i] = (dic[i][0], dic[i][1] + 1)

res = 0
temp = 0
for idx in sorted(dic.keys()):
    member = dic[idx]
    # 현재 상태에 temp를 반영하여 새로운 튜플 생성
    pre_updated_member = (member[0] + temp, member[1])
    if pre_updated_member[1] >= T:
        # 부끄러워서 다 집감 (guest의 방문을 초기화)
        pre_updated_member = (0, pre_updated_member[1])
        temp = 0
        # 신 강림함
        res += 1
    elif pre_updated_member[1] < T and friend >= 0:
        friend -= 1
        temp += 1
        after_updated_member = member[0] + temp, member[1]
        if after_updated_member[0] + after_updated_member[1] >= T:
            res += 1
    dic[idx] = pre_updated_member

print(res)

"""

"""

# N, M, K, T = map(int, sys.stdin.readline().rstrip().split(" "))
# start = [0] * (N + 1)
# end = [0] * (N + 2)
# # 각 기도 시작시간, 끝나는 시간을 저장
# for _ in range(M):
#     x, y = map(int, sys.stdin.readline().rstrip().split(" "))
#     start[x] += 1
#     end[y] += 1
# # 시작시간
# time = 1
# # 현재 기도인원
# pray_now = 0
# # 투입된 친구
# friend = 0
# # 시작은 전체 N 만큼 볼 수 있음, 그 중 없는것을 뺌
# answer = N
# 
# for i in range(1,N+1):
#     # 현재 기도하고 있는 인원 체크 더해줌, (친구는 없이)
#     pray_now += start[time] - end[time]
#     # 친구들이 나가도 알빠 아님
#     if pray_now - friend >= T:
#         pray_now -= friend
#         friend = 0
#     # 신도들이 부족함
#     elif pray_now < T:
#         # 필요한 친구들 구해줌
#         need_prey_people = T - pray_now
#         # 남은 친구들보다 필요한 친구가 더 많이 필요함 엘리스가 강림할 수 없음
#         if K < need_prey_people:
#             # 강림할 수 없는 시간 빼줌
#             answer -= 1
#             # 다음 시간 ㄱ
#             continue
#         # 가능하면 기도중인친구들, 기도할수 있는친구들, 현재 기도중인 친구들로 업데이트
#         K -= need_prey_people
#         friend += need_prey_people
#         pray_now = T
#     time += 1
# 
# print(answer)
"""

input = __import__("sys").stdin.readline
n, m, l, t = map(int, input().split())
a = [0] * n
for _ in range(m):
    i, j = map(int, input().split())
    for k in range(i - 1, j - 1):
        a[k] += 1
d = [0] * -~l
c = [0] * -~t
for i in range(n):
    if a[i] >= t:
        while len(c) > 1 and not c[-1]:
            c.pop()
        for i in range(len(c) - 1):
            c[i + 1] += c[i]
        d = [
            max(d[i - j] + c[j] for j in range(min(i + 1, len(c)))) + 1
            for i in range(l + 1)
        ]
        c = [0] * -~t
    else:
        c[t - a[i]] += 1
while len(c) > 1 and not c[-1]:
    c.pop()
for i in range(len(c) - 1):
    c[i + 1] += c[i]
d = [max(d[i - j] + c[j] for j in range(min(i + 1, len(c)))) for i in range(l + 1)]
print(d[-1])
