# def solution(lotteries):
#     # 확률
#     per = []
#     for idx,details in enumerate(lotteries):
#         per.append((idx,details[0]/(details[1]+1),details[2]))
#
#     per.sort(key=lambda x:(-x[1],-x[2]))
#     return per[0][0] +1
#
# lotteries [당첨자, 구매자, 당첨금]
# # print(solution([[100, 100, 500], [1000, 1000, 100], [100, 100, 600]]))
# print(solution([[10, 19, 800], [20, 39, 200], [100, 199, 500]]))

def solution(grid):
    board = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    dx=[-1,0,1,0,-1,-1,1,1]
    dy=[0,1,0,-1,-1,1,-1,1]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for z in range(8):
                xx = x + dx[z]
                yy = y + dy[z]
                # print(xx,yy)
                if 0 <= xx < len(grid) and 0 <= yy <len(grid[0]) and grid[xx][yy] == "#"  :
                    board[xx][yy] = 1
    return (sum(board,[]).count(1))

# 000001111
# 001000111
# 010110011
# 001001000
# 001000100
# 000111000
#
# 1111
# 1101
# 0101





# print(solution([".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#..", "...###..."])) 27
# print(solution([".#.", "#..", ".#."]))
# print(solution(["####", "##.#", ".#.#"]))
def solution1(queries):
    res = []
    for query in queries:
        count = 0
        while query != list(reversed(query)):
            left, right = 0, -1
            while query[left] or query[right] != 0:
                if query[left] == query[right]:
                    break
                if query[left] >= query[right]:
                    query[left] -= 1
                    count += 1
                else:
                    query[right] -= 1
                    count += 1
                if left < len(query) // 2 and -1 * right < len(query) // 2:
                    left += 1
                    right -= 1
        res.append(count)
    result = [1 if i % 2 == 0 else 2 for i in res]

# print(solution1([[2, 0], [3, 1]]))
print(solution1([[0, 2, 0, 1], [0, 1, 0, 1]]))

# (2,0) > (1,0) > (0, 0) : 2번 두번째 승
# (3,1) > (2,1) > (1,1) : 2번 2번째 승

