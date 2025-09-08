import itertools

def sosu(n):
    if n < 2:
        return 0
    else:
        for i in range(2, n):
            if n%i == 0:
                return 0
        return 1

def solution(nums):
    answer = 0
    combination = list(itertools.combinations(nums, 3))
    # print(combination)
    for i in range(len(combination)):
        answer += sosu(sum(combination[i]))

    return answer

print(solution([1,2,3,4]))