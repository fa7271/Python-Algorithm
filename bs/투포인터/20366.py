import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(input())
lst = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))

res = 1e9
for i in range(N - 3):
    for j in range(i + 3, N):
        # 밖에 있는 i, j
        left = i + 1;
        right = j - 1
        while left <= right:
            middle_res = (lst[i] + lst[j]) - (lst[left] + lst[right])
            if abs(middle_res) < res:
                res = abs(middle_res)
                if res == 0:
                    print(res)
                    exit()
            if middle_res < 0:
                right -= 1
            else:
                left += 1
print(res)
