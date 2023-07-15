
import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

def find_parent(parent, x):
    result = [x]
    while parent[x]:
        result.append(parent[x])
        x = parent[x]
    return result


result = []
N = int(input()) # 16
parent = [0 for _ in range(N+1)]
for i in range(N-1):
    x, y = map(int, sys.stdin.readline().rstrip().split(" ")) # x 가 y의 부모
    parent[y] = x
print(parent)
m = int(sys.stdin.readline())
for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    lst_a = find_parent(parent,x)
    lst_b = find_parent(parent,y)
    if len(lst_a) > len(lst_b):
        lst_a = lst_a[-len(lst_b):]
    else:
        lst_b = lst_b[-len(lst_a):]
    print(lst_a,lst_b)
#     depth = 0
#     while lst_a[depth] != lst_b[depth]:
#         depth += 1
#     result.append(depth)