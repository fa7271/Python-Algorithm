import sys
from collections import deque, defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(sys.stdin.readline().rstrip())
names = sorted(list(map(str,sys.stdin.readline().rstrip().split())))
m = int(sys.stdin.readline().rstrip())
parents = defaultdict(list)
childs = defaultdict(list)
indegree = {i:0 for i in names}
for _ in range(m):
    child, parent = input().split()
    parents[parent].append(child)
    indegree[child] += 1
Q = deque()
root = []
for name in names:
    if indegree[name] == 0:
        Q.append(name)
        root.append(name)
print(len(root))
print(*root)
while Q:
    node = Q.popleft()
    for next_node in parents[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            Q.append(next_node)
            childs[node].append(next_node)
for i in names:
    res = i + " " + str(len(childs[i])) + " "
    if len(childs[i]) != 0:
        res += " ".join(sorted(childs[i]))
    print(res)
