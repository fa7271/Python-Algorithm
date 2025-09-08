import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n, m =map(int,sys.stdin.readline().split(" "))
lst = sorted([int(input()) for _ in range(n)])
targrt_lst = [int(input()) for _ in range(m)]
def bisec(lst , target):
    left = 0; right = len(lst)-1
    while left <= right:
        mid = (left + right) // 2 # 중간 값
        if lst[mid] < target :
            left = mid + 1
        elif lst[mid] > target: #
            right = mid - 1
        elif lst[mid] == target:
            # 해당 숫자가 가장 먼저 시작 되는 곳까지 간다.
            if right == mid:
                break
            right = mid
    if lst[mid] == target:
        return mid
    else:
        return -1
for i in targrt_lst:
    print(bisec(lst, i))
    break


# bisect_left(lower) bisect_right 지