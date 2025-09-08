import sys
from collections import deque

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = deque(sorted([list(map(int,sys.stdin.readline().split(" "))) for _ in range(n)], key = lambda x:x[0]))

# 투포인터
left, right = lst.popleft()
lines = 0

while lst:
    start, end = lst.popleft()

    # 시작하는 선에 right 값이 다음 들어오는 끝값보다 크면 굳이 체크 x
    # 즉 이미 있는 선 안에 겹치게 된다.
    if right >= end:
        continue

    # 시작하는 선에 right 값이 다음 선 end 값과 사이에 있으면 right 값을 옮겨줘야함
    # 즉 겹치는 선이면서 길이가 더 길어 진다.
    elif start <= right < end:
        right = end
    else:
        # 이어진 선 완성
        lines += right - left
        # 안 겹치는 새로운 선 만들
        left = start
        right = end
lines += right - left
print(lines)

    # if start <= right:
    #     lines += end - right
    #     left = right
    # if start > right:
    #     left = start
    #     right = end
    #     lines += end - start

# 13
# 25
# 35
# 67