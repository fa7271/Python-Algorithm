def solution(wallpaper):
    n, m = len(wallpaper), len(wallpaper[0])
    s_x, s_y, l_x, l_y = 51, 51, 0, 0
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == "#":
                s_x = min(s_x, i)
                s_y = min(s_y, j)
                l_x = max(l_x, i)
                l_y = max(l_y, j)
    return s_x,s_y,l_x + 1,l_y + 1

# print(solution([".#...", "..#..", "...#."]))
print(solution(	["..........", ".....#....", "......##..", "...##.....", "....#....."]))