import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt','r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())
import math
cases = int(input())
results = []

for case in range(cases):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    ps = int(input())
    planets = []
    for p in range(ps):
        px, py, pr = map(int, input().split())
        # 출발지와 원의 중심 사이의 거리
        d1 = math.sqrt((x1 - px) ** 2 + (y1 - py) ** 2)
        # 도착지와 원의 중심 사이의 거리
        d2 = math.sqrt((x2 - px) ** 2 + (y2 - py) ** 2)
        # 출발지 또는 도착지가 중심 사이의 거리보다 작다면 진입/이탈
        if d1 < pr or d2 < pr:
            # 이지만 둘 다 포함하는 경우는 패스
            if d1 < pr and d2 < pr: pass
            else: count += 1
    results.append(count)

for result in results:
    print(result)