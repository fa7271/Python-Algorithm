import math
from itertools import product


# def solution(n):
#     words = ["1","2","4"]
#     count = n
#     list =[]
#     while count >= 0:
#         for i in range(1,int(math.sqrt(n)) + 1):
#             for j in product(words, repeat = i):
#                 list.append("".join(j))
#                 count -= 1
#     print(list[n-1])

    # words = ["1","2","4"]
    # list = []
    # count = n
    # if n == 1 : return "1"
    # while True:
    #     for i in range(1,n):
    #         for j in product(words, repeat = i):
    #             list.append("".join(j))
    #             if len(list) == n:
    #                 return list[-1]

def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        print(answer)
        n //= 3
    return answer
print(solution(999))
