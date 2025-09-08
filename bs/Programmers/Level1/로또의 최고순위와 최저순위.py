
def solution(lottos, win_nums):
    rank = {6 : 1, 5 : 2 , 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0: 6}

    win = list(set(lottos)&set(win_nums))
    if lottos.count(0) == 6:
        return [1 , (rank[len(win)])]
    else:
        return [rank[len(win)] - lottos.count(0),(rank[len(win)])]



print(solution(	[45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35] ))