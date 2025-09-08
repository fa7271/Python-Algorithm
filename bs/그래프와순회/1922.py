import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
M = int(input())
graph = []

# 부보 자기자신 초기화
parent = [i for i in range(N+1)]

# 간선 저장
for i in range(M):
    a, b, c = map(int,sys.stdin.readline().rstrip().split(" "))
    graph.append((a,b,c))
# 가중치 값 기준 정렬
graph.sort(key= lambda x:x[2])
# 부모 찾기
def find(node):
    # 자기자신과 부모노드가 다를경우
    if node != parent[node]:
        #부모를 찾아야함 , >> 부모의 부모를 찾아야함
        parent[node] = find(parent[node])
    return parent[node]
def union(a, b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
res = 0

for node1, node2, e in graph:
    a_root = find(node1)
    b_root = find(node2)

    if a_root != b_root:
        union(a_root, b_root)
        res += e
print(res)


