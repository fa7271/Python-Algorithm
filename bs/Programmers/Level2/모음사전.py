from itertools import  product


def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    list = []
    for i in range(1,6):
        for j in product(words, repeat = i):
            list.append("".join(j))
    return  sorted(list).index(word) + 1




print(solution("AAAAE"))



