import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

# 시간 초과
# 1. 탐색하는 Numbers에 숫자를 이미 배치된 숫자를 빼고 함 -> 50%
# 2. is_possibe 을 자주 호출함

n = int(input())
lst = list(map(int, sys.stdin.readline().split()))

# 가로 체크
col = [False] * (n + 1)
up = [False] * (2 * n)
down = [False] * (2 * n)
nums = sorted(set(range(1, n + 1)) - set(lst))

def bt(i):
    if i == n:
        print(*lst)
        exit()
    if lst[i]:  # 이미 퀸이 놓인 경우
        if not (col[lst[i]] or up [i-lst[i] +n ] or down[i + lst[i]]):
            col[lst[i]] = up[i-lst[i] +n ] = down[i + lst[i]] = True
            bt(i+1)
            col[lst[i]] = up[i-lst[i] +n ] = down[i + lst[i]] = False
        return

    for j in nums:  # 퀸 둬야함
        if not (col[j] or up[i - j + n] or down[i + j]):
            lst[i] = j
            col[j] = up[i - j + n] = down[i + j] = True
            bt(i + 1)
            col[j] = up[i - j + n] = down[i + j] = False
            lst[i] = 0

bt(0)
print(-1)