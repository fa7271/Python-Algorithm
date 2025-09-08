def solution(n):

    # num_list = list(map(int, str(n)))
    # return sum(num_list)

    return sum([int(i) for i in str(n)])

print(solution(123))