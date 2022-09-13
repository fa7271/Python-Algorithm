def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    res = [0, 0, 0]
    result = []
    for count, answers in enumerate(answers):
        if answers == one[count % len(one)]:
            res[0] += 1
        if answers == two[count % len(two)]:
            res[1] += 1
        if answers == three[count % len(three)]:
            res[2] += 1

    for count, i in enumerate(res):
        if i == max(res):
            result.append(count+1)

    return result




print(solution([1,3,2,4,2,3]))