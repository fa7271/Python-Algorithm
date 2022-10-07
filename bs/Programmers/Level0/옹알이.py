def solution(babbling):

    can = ["aya", "ye", "woo", "ma"]

    for i in range(len(babbling)):
        for j in range(4):
            if can[j] +can[j] in babbling[i]:
                continue
            if can[j] in babbling[i]:
                babbling[i] = babbling[i].replace(can[j],"")
    return babbling.count('')
print(solution(	["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
