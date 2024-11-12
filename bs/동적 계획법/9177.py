import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())

for i in range(N):
    A, B, C = input().split()
    Q = deque([(0, 0, 0)])
    visited = [[0] * (len(B)+1) for _ in range(len(A)+1)]

    visited[0][0] = True
    flag = False
    while Q:
        left, right, idx = Q.popleft()
        if idx == len(C):
            flag = True
            break
        if left < len(A) and not visited[left + 1][right] and A[left] == C[idx]:
            print("left:",left,right,idx)
            Q.append((left + 1, right, idx + 1))
            visited[left + 1][right] = True
        if right < len(B) and not visited[left][right + 1] and B[right] == C[idx]:
            print("right:",left,right,idx)
            Q.append((left, right + 1, idx + 1))
            visited[left][right + 1] = True
    print(visited)
    exit()
    if flag:
        print(f"Data set {i+1}: yes")
    else:
        print(f"Data set {i+1}: no")