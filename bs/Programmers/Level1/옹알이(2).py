from itertools import product

def solution(babbling):
    result = 0

    for word in babbling:
        stack = ''
        prev = ''

        for char in word:
            stack += char
            if prev != stack and (stack == 'aya' or stack == 'ye' or stack == 'woo' or stack == 'ma'):
                prev = stack
                stack = ''
        if len(stack) == 0:
            result += 1

    return result

# def solution(babbling):
#     n = ["aya", "ye", "woo", "ma"]
#     for k, i in enumerate(babbling):
#         for j in n:
#             if j*2 in i:
#                 break
#             babbling[k]=babbling[k].replace(j, " ")
#         babbling[k]=babbling[k].replace(" ", "")
#     return babbling.count("")

# for i in babbling:

# for i in len(babbling):
#     for j in speak:
#         can = ''
#         if j in i:
#             can += j




# print(solution(	["aya", "yee", "u"]))
print(solution(	["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))

# from itertools import product
# def solution(babbling):
#     speak = ["aya", "ye", "woo", "ma" ]
#     count = 0
#     for j in babbling:
#         for i in range(1,5):
#             if j in list(map(''.join, product(speak, repeat = i))):
#                 count += 1
#     return count