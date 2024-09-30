import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, k = map(int, sys.stdin.readline().rstrip().split())
arr = deque(list(map(int, sys.stdin.readline().rstrip().split())))
# 로봇 체크
belt = deque([False] * n)

answer = 0
# for i in range(n-2,-1,-1):
#     print(i)
while arr.count(0) < k:

    answer += 1

    # 1, 오른쪽 가기
    arr.rotate(1)
    belt.rotate(1)
    # 내리는 위치에 있으면  내림
    belt[n - 1] = False

    # 2. 한칸씩 이동하기, 못 가면 가만히 있고
    for i in range(n - 2, -1, -1):
        # 아무것도 없고 내구도 있어야함
        if belt[i] and not belt[i + 1] and arr[i + 1] > 0:
            belt[i] = False
            belt[i + 1] = True
            arr[i + 1] -= 1
    belt[n - 1] = False

    # 3. 올리는 칸 내구도 0 아니면 올림
    if arr[0] > 0:
        belt[0] = True
        arr[0] -= 1
print(answer)
