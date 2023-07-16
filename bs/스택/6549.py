import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

while True:
    n, *heights = map(int, input().split())
    if n == 0:
        break

    stack = []  # 높이를 저장할 스택
    max_area = 0  # 가장 큰 직사각형의 넓이
    for i in range(n):
        while stack and heights[i] < heights[stack[-1]]: # 스택이 있고, 다음 건물 높이가 스택 마지막 보다 낮을때까지
            height = heights[stack.pop()] # 높이는 스택 마지막 건물 높
            width = i if not stack else i - stack[-1] - 1 # i번째 까지의 최소 높이
            area = height * width # 면적
            max_area = max(max_area, area) # 최대 면적 구해준다.
        stack.append(i) # 스택이 비어있으면
    while stack: # 스택이 남아있으며 예제2번같이 똑같이 해준다.
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        area = height * width
        max_area = max(max_area, area)

