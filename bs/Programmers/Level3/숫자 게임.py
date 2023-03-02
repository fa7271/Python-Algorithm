from collections import deque
def solution(A, B):
    idx = 0
    A = deque(sorted(A))
    B = deque(sorted(B))
    count = 0
    while len(B) > 0 and len(A) > 0:
        left, right = A.popleft(), B.popleft()
        if right > left :
            count += 1
        else:
            idx += 1
            A.appendleft(left)
    return count





print(solution([5, 1, 3, 7], [1, 2, 6, 8]))