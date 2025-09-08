def solution(numbers):
    res = []
    for number in numbers:
        number = int(number)
        if number % 2 == 0:
            res.append(number+1)
        else:
            now = '0' + bin(number)[2:]
            index = now.rfind("0")
            now_list = list(now)
            now_list[index] = "1"
            now_list[index+1] = "0"
            res.append(int("".join(now_list),2))
    return res






print(solution([2, 7]))
# if bin(n+1)[2:]


