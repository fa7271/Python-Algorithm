
import sys
from collections import defaultdict

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m, k = map(int, sys.stdin.readline().split())

# 비용기준 정렬
A = [0] + [cost for cost in list(map(int,sys.stdin.readline().split()))]

# 처음 부모는 자기 자신
parents = [i for i in range(n+1)]
def find(x):
    # 자기자신이 부모가 아니면
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

# 작은 비용으로 union 해줌
def union(a, b):
    a = find(a)
    b = find(b)

    if A[a] < A[b]:
        parents[b] = a
    else:
        parents[a] = b
# 누가 더 작은 지 찾아봄
for i in range(m):
    v, w = map(int, sys.stdin.readline().split())
    # 부모 찾기
    # 합쳐야함 원래는 작은수로 합치지만, 이 문제에선 작은 비용 기준으로 해야한다.
    union(v, w)
ans = 0
for idx, res in enumerate(parents):
    if idx == res:
        ans += A[idx]
if ans <=k:
    print(ans)
else:
    print("Oh no")

# 19학번 이준석은 학생이 N명인 학교에 입학을 했다. 준석이는 입학을 맞아 모든 학생과 친구가 되고 싶어한다.
# 하지만 준석이는 평생 컴퓨터랑만 대화를 하며 살아왔기 때문에 사람과 말을 하는 법을 모른다. 그런 준석이에게도 희망이 있다. 바로 친구비다!
# 학생 i에게 Ai만큼의 돈을 주면 그 학생은 1달간 친구가 되어준다! 준석이에게는 총 k원의 돈이 있고 그 돈을 이용해서 친구를 사귀기로 했다.
# 막상 친구를 사귀다 보면 돈이 부족해질 것 같다는 생각을 하게 되었다. 그래서 준석이는

# “친구의 친구는 친구다”를 이용하기로 했다.

# 친구비 최솟값 heapq ??
