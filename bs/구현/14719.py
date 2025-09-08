import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

H, W = map(int,input().split(" ")) # H 가로 W 세로

maps = [[0]*H for i in range(W)]
print(maps)

lst = list(map(int,input().split(" ")))

res = 0
for i in range(1, W - 1): # 첫째 칸과 마지막 칸은 물이 안 고임
    left_max = max(lst[:i])
    right_max = max(lst[i+1:])
    min_num = min(left_max, right_max)

    # 빗물 고이는 곳이 양 옆으로 높은곳이 있으면 물이 잠긴다. 그럼 그 작은 높이의 벽돌과 내 벽돌 차이만큼 물이 찬다.
    if lst[i] < min_num:
        res += min_num - lst[i]

print(res)

