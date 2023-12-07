import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

n = int(input())

# y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    total_distance = y - x # 총 이동해야 하는 거리

    now_move = 1 # 시작 광년
    next_move = 1 # 거리
    count = 0 # 횟수
    while next_move <= total_distance:
        count += 1
        next_move += now_move
        if count % 2 == 0:
            now_move += 1
    print(count)

    # 1 > 1
    # 2 > 1 1
    # 3 > 1 1 1
    # 4 > 1 2 1 > 1 1 2
    # 5 > 1 2 1 1 > 1112
    # 6 > 1 2 2 1 > 1122
    # 7 >  1 2 2 1 1 > 11122
    # 8 > 1 2 3 2 1 > 11223
    # 2 제외 하고 짝수 번째에 next_move 가 증가됨