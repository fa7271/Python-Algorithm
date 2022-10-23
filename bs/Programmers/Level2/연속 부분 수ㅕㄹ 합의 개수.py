from itertools import combinations
def solution(elements):

    # elements_set = set ()
    # for i in range(1, len(elements) +1 ):
    #     for j in list(combinations(elements,i)):
    #         print(j)
    #         elements_set.add(sum(j))
    # return len(elements_set)
    #
    elements_set = set()
    for i in range(len(elements)):
        for j in range(i, len(elements) + 1):
            print(elements[i:j+1],elements[j-len(elements) : i])
            elements_set.add(sum(elements[i:j]))
print(solution(	[7,9,1]))

#