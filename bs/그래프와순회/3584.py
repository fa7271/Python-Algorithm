
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')


# 부모 찾기 위한 함수
def find_parent(parent, x):
    # 자기자신은 자기가 부모
    result = [x]
    # x의 부모가 존재 하는 동안
    while parent[x]:
        # 부모를 넣어주고
        result.append(parent[x])
        # 부모의 부모를 찾기위해 x를 부모로 바꿔준다.
        x = parent[x]
    # 다 찾았으면 그대로 결과값 리턴
    return result

T = int(input())
for _ in range(T):
    N = int(input())
    # 부모 처음은 자기자신이 부모이다.
    parent = [0 for _ in range(N+1)]
    for _ in range(N-1):
        x, y = map(int,sys.stdin.readline().split(" "))
        # y의 부모는 x
        parent[y] = x
    # 마지막 찾을 노드
    a, b = map(int, input().split())
    # 자기 자신 포함 부모 찾기
    lst_a = find_parent(parent,a)
    lst_b = find_parent(parent,b)

    x, y = 0,0
    # lst_a의 깊이가 더 깊은 경우 b만큼 길이만 필요하다.
    if len(lst_a) > len(lst_b):
        lst_a = lst_a[-len(lst_b):]
    else:
        lst_b = lst_b[-len(lst_a):]

    # 잘린거 기준으로 앞에서 부터 비교
    depth = 0
    while lst_a[depth] != lst_b[depth]:
        depth += 1
    print(lst_a[depth])