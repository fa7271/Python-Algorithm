from itertools import combinations
def solution(elements):

    # elements_set = set ()
    # for i in range(1, len(elements) +1 ):
    #     for j in list(combinations(elements,i)):
    #         print(j)
    #         elements_set.add(sum(j))
    # return len(elements_set)
    #
    # elements_set = set()
    # for i in range(len(elements)):
    #     for j in range(i+1, len(elements) + 1):
    #         print(elements[i:j],elements[:i])
    #         elements_set.add(sum(elements[i:j]))
    elements_set = set(i for i in elements)
    elements = 2 * elements
    for i in range((len(elements)//2)):
        for j in range(2,(len(elements)//2) + 1):
            elements_set.add(sum(elements[i:i+j]))
    return (len(elements_set))
print(solution(	[7,9,1,1,4]))

#