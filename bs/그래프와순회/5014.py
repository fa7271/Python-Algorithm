import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
sys.setrecursionlimit(10**6)
F, S, G, U, D = map(int, input().split(" "))
if S == G:
    print(0)
    exit()
graph = [0] * (F + 1)
graph[S] = 1
def dfs(node):
    if node == G:
        print(graph[node] -1)
        exit()
    for next_node in [node + U, node - D]:
        if 0 < next_node <= F and graph[next_node] == 0:
            graph[next_node] = graph[node] + 1
            dfs(next_node)
dfs(S)
print("use the stairs")
