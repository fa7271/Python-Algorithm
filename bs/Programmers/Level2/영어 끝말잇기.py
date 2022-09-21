
def solution(n, words):
    print(words[1][0])
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]: # 끝말잇기가 아니거나 이미 앞에 있는경우
            return [ (i%n) + 1 , (i//n)+1 ]
    else:
        return [0, 0]




print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
