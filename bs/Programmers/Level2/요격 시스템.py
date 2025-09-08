
def solution(targets):
    targets = sorted(targets, key = lambda x:x[1])
    res = 1
    now = targets[0][1] # 4
    for i in range(1, len(targets)):
        if now <= targets[i][0]:
            now = targets[i][1]
            res += 1




print(solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]))