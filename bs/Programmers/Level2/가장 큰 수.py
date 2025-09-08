from itertools import permutations, product
from collections import deque

# def solution(numbers):
#     res = list(permutations(numbers, len(numbers)))
#     num_str = []
#     for i in range(len(res)):
#         num_str.append("".join(map(str,res[i])))
#     return(max(num_str))
def solution(num):

    num = list(map(str, num))
    num.sort(key = lambda x : x*3, reverse = True)

    return str(int(''.join(num)))
print(solution([3, 30, 34, 5, 9]))

# def solution(word):
#     words = ['A', 'E', 'I', 'O', 'U']
#     list = []
#     for i in range(1,6):
#         for j in product(words, repeat = i):
#             list.append("".join(j))