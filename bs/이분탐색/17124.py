import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

t = int(input())
for _ in range(t):
    n, m = map(int,sys.stdin.readline().split(" "))
    list_A = list(map(int,sys.stdin.readline().split(" ")))
    list_B = sorted(list(map(int,sys.stdin.readline().split(" "))))
    count = 0

    #  A 에 가까운 수열
    res = []
    for num in list_A:
        left = 0; right = m - 1
        while left < right:
            mid = (left + right) // 2
            if list_B[mid] <= num: # 타겟 넘버보다 작으면 왼쪽 올려줌
                left = mid + 1
            else:
                right = mid
        if left == 0 :
            # 그 위치가 0 이면
            count += list_B[0]
        else:
            # 아닐때 앞에 꺼 보다 큰 값인지 비교해줘야함
            count += list_B[left] if num - list_B[left-1] > list_B[left] - num else list_B[left-1]
    break

    # A = 5 9 14 20
    # B = 8 12 16
