import sys

sys.stdin = open('/Python/h.txt', 'r')

# input = sys.stdin.readline
# input = int(sys.stdin.readline())

T = int(sys.stdin.readline())
distance = 0    # 대각
for i in range(T):
    x1,y1,r1,x2,y2,r2 = list(map(int,(sys.stdin.readline().split())))

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5      # 점 들 사이의 거리 피타고리스 사용
    a = r1 + r2         #  두 반지름의 합
    b = abs(r1-r2)      #  두 반지름의 차

    if distance == 0:       #두 원의 중심이 같은 경우
        if r1 == r2 :
            print(-1)
        else:
            print(0)
    else:                           # 두 원의 중심이 다른경우
        if distance == a or distance == b:          # 원이 접할때
            print(1)
        elif distance < a and distance > b :        # 두개의 점이 접할때
            print(2)
        else:
            print(0)

# 만약 이렇게 접점이 2개가 생기는 경우에는 두 반지름의 합(r + r')이 중심 거리(d)보다 큰 경우이다.
#
# 단, 여기서 주의해야할 점은 중심 거리(d)가 두 반지름의 차(r - r')보다는 커야한다는 점이다.
#

