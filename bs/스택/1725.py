import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

stk = []
max_area = 0

for i in range(N):
    while stk and lst[i] < lst[stk[-1]]: # 높이가 뚝 떨이지는 경우 앞에꺼 계산해줌
        H = lst[stk.pop()] # 높이
        width = i if not stk else i - stk[-1] - 1 # i번째 까지의 최소 높이
        area = H * width # 면적
        max_area = max(max_area, area) # 최대 면적
    stk.append(i) # 스택이 비어있으면

while stk: # 스택이 남아 있는경우
    height = lst[stk.pop()]
    width = N if not stk else N - stk[-1] - 1
    area = height * width
    max_area = max(max_area, area)

print(max_area)
