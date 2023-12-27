import sys
sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}
number = {"A":1,
          "B":2,
          "C":3,
          "D":4,
          "E":5,
          "F":6,
          "G":7,
          "H":8}
target, start, n = list(input().split(" "))
king = [number[target[0]], int(target[1])]
stone = [number[start[0]], int(start[1])]
for i in range(int(n)):
    mo = input()
    nx = king[0] + move[mo][0]; ny = king[1] + move[mo][1]
    if 0 < nx <= 8 and 0 < ny <= 8 :
        # 킹이 벽돌로 가고,
        if nx == stone[0] and ny == stone[1]:
            # 킹이 가는 방향으로 간다.
            sx = stone[0] + move[mo][0]
            sy = stone[1] + move[mo][1]
            if 0<sx<=8 and 0<sy<=8:
                king = [nx,ny]
                stone = [sx,sy]
        else:
            king = [nx,ny]
for i in king, stone:
    for key, value in number.items():
        if i[0] == value:
            print(key+str(i[1]))


