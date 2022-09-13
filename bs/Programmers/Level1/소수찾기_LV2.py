from itertools import permutations

def solution(n):
    numbers = [i for i in n]

    com_list = []
    for i in range(1, len(numbers) + 1):
        com_list += list(permutations(numbers, i))
    # com_list2 = sum([ list(permutations(numbers, i)) for i in range(1, len(numbers) + 1)],[])

    new_list = set(int(("").join(i)) for i in com_list)
    new_list_len = len(new_list)
    print(new_list_len,new_list)

    for i in new_list:
        if i < 2:
            new_list_len -= 1
        for j in range(2, int(i**0.5) +1 ):
            if i%j ==0:
                new_list_len -=1
                break
    return new_list_len



print(solution("011"))