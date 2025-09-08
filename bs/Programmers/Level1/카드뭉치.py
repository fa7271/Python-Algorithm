
def solution(cards1, cards2, goal):

    for x in goal:
        print(x)
        if len(cards1)>0 and cards1[0] == x:
            cards1.pop(0)
        elif len(cards2) > 0 and cards2[0] == x:
            cards2.pop(0)
        else:
            return "x"
    return "yes"
print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
# print(solution(	["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))