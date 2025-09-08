import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())
lst = sorted(map(int, sys.stdin.readline().rstrip().split(" ")))
print(lst)
# 같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다.
# 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.

# 투 포인터

# 양 끝으로 포인터 설정
start = 0
end = n - 1

# 초기 값 설정
res = abs(lst[start] + lst[end])
res_lst = [lst[start], lst[end]]
while start < end:
    # 처음은 양 끝 값의 합
    left = lst[start]
    right = lst[end]

    res_temp = left + right
    # 기존보다 작으면
    if abs(res_temp) < res:
        # 그걸로 바꿔주고
        res = abs(res_temp)
        # 정답값도 바꿔주고
        res_lst = [left, right]
        # 0이면 가장 베스트라 끝냄
        if res == 0:
            break

    # 0 보다 크면 오른쪽을 줄여봄
    if res_temp < 0:
        start += 1
    else:
        end -= 1
print(*res_lst)
