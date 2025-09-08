import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')
from collections import deque

N, L = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, input().split()))

# 최솟값 담을예정, (인덱스랑, 밸류값)
result = deque([])
answer = []
for idx in range(len(arr)):

    # 배열이 있고, 처음과 마지막 뺀 인덱스 값이 L 갯수 이하여야함.
    # 슬라이딩 윈도우 범위 벗어나면 없애버림

    if result and result[0][0] <= idx - L:
        result.popleft()

    # 새로 들어온 숫자가 기존 숫자보다 크면 쑥 밀어버림
    while len(result) >= 1 and arr[idx] < result[-1][1]:
        result.pop()
    result.append((idx,arr[idx]))
    print(result[0][1])

    # 인덱스와 그 인덱스 값 추가.
    # print(result[0][1], end=" ")

# 12 3
# 1 5 2 3 6 2 3 7 3 5 2 6
# 1 1 1 2 1 1 1 2 3 3 2 2
# 1 1 2 2 2 2 2 2 3 3 2 2
