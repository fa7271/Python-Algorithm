def solution(n, lost, reserve):

    reserve_p = set(reserve) - set(lost)
    lost_p = set(lost) - set(reserve)


    for i in reserve_p:
        print(lost_p)
        be = i - 1
        af = i + 1
        print(be, af , reserve_p)
        if be in lost_p:
            lost_p.remove(be)
        elif af in lost_p:
            lost_p.remove(af)
    return n - len(lost_p)

print(solution(5,[2, 4],[3]))